#!/bin/bash
SSH_USER='alex'
SRC_DIRECTORY='/home/alex/scraping-infra'
source .env

CURRENT_BRANCH="$1"

if [[ -z "$CURRENT_BRANCH" ]]; then
    read -p "Enter the branch you want to set " CURRENT_BRANCH
fi

function PULL_REPO() {
    SSH_CMD="cd $SRC_DIRECTORY && git checkout $CURRENT_BRANCH && git pull"
    echo "Pulling repo at $SSH_USER@$1"
    ssh "$SSH_USER"@$1 "$SSH_CMD"
}

function REBUILD_DOCKER_IMAGE() {
    local host=$1
    local new_packages=$2

    SSH_CMD="cd $SRC_DIRECTORY && \
             docker compose -f docker-compose.yml stop && \
             docker build -t scraping_infra:latest -f compose/Dockerfile \
             --build-arg NEW_PACKAGES=\"$new_packages\" \
             ."
    ssh "$SSH_USER"@$host "$SSH_CMD"
    echo "Rebuilt Docker image successfully at $host." 
}

function RESTART_CONTAINER() {
    SSH_CMD="cd $SRC_DIRECTORY && docker compose -f docker-compose.yml restart $2"
    ssh "$SSH_USER"@"$1" "$SSH_CMD"
}

function UPDATE_CODE() {
    IFS=' ' read -ra HOSTS <<< "$HOSTS"
    host=`echo $HOSTS | cut -d "@" -f 1`
    
    # Compare local requirements.txt content with the one on a remote machine
    scp $SSH_USER@$host:$SRC_DIRECTORY/requirements.txt ./requirements_remote.txt
    DIFF_OUTPUT="$(diff ./requirements.txt ./requirements_remote.txt)"
    rm ./requirements_remote.txt

    if [ -n "$DIFF_OUTPUT" ]; then
        echo "Requirements have been updated. Packages will be installed."
        PIP_FLAG=1
    else
        echo "Requirements have not been touched. Skipping libraries update"
        PIP_FLAG=0
    fi

    # Extract the missing packages
    if [ "$PIP_FLAG" -eq 1 ]; then
        missing_packages=$(python <<END
import subprocess
with open("requirements.txt") as f:
    requirements = set(f.read().splitlines())
installed_packages = subprocess.check_output(['pip', 'freeze']).decode().splitlines()
missing_packages = sorted(list(requirements - set(installed_packages)))
print(" ".join(missing_packages))
END
)
        echo "Missing packages: $missing_packages"
    fi

    for host in "${HOSTS[@]}"; do
        PULL_REPO $host 
        if [ "$PIP_FLAG" -eq 1 ]; then
            REBUILD_DOCKER_IMAGE $host "$missing_packages"
            if ! [ $? -eq 0 ]; then
                echo "Error: REBUILD_DOCKER_IMAGE failed for $host. Stopping pipeline"
                exit 1
            fi
        fi
    done
}

function RESTART_ENVIRONMENT() {
    for conn in $CELERY_SERVICES; do
        host=$(echo $conn | cut -d "@" -f 1)
        celery_service=$(echo $conn | cut -d "@" -f 2)
        RESTART_CONTAINER $host $celery_service &
        if ! [ $? -eq 0 ]; then
            echo "Error: RESTART_CONTAINER failed for $celery_service at $host. Stopping pipeline"
            exit 1
        fi
    done
    wait
}


UPDATE_CODE
RESTART_ENVIRONMENT
