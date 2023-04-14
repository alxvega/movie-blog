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
    SSH_CMD="cd $SRC_DIRECTORY && /usr/local/bin/docker build -t scraping_infra -f compose/Dockerfile . && docker compose -f docker-compose.yml down && docker compose -f docker-compose.yml up -d $2"
    ssh "$SSH_USER"@$1 "$SSH_CMD"
    echo "Rebuilt Docker image and restarted container for service $2 successfully." 
}

function RESTART_CONTAINER() {
    SSH_CMD="cd $SRC_DIRECTORY && docker compose -f docker-compose.yml restart $2"
    ssh "$SSH_USER"@"$1" "$SSH_CMD"
}

function UPDATE_CODE() {
    IFS=' ' read -ra HOSTS <<< "$HOSTS"
    host=`echo $HOSTS | cut -d "@" -f 1`
    echo "Getting requirements.txt from $SSH_USER@$host:$SRC_DIRECTORY"
    scp $SSH_USER@$host:$SRC_DIRECTORY/requirements.txt ./requirements_remote.txt
    PIP_STATUS="$(cmp -s ./requirements_remote.txt /home/alex/scraping-infra/requirements.txt; echo $?)"
    rm ./requirements_remote.txt

    if [ "$PIP_STATUS" -eq 1 ]; then
        echo "Requirements have been updated. Packages will be installed."
        PIP_FLAG=1
    else
        echo "Requirements have not been touched. Skipping libraries update"
        PIP_FLAG=0
    fi

    for host in "${HOSTS[@]}"; do
        PULL_REPO $host 
        if [ "$PIP_FLAG" -eq 1 ]; then
            for conn in $CELERY_SERVICES; do
                host_service=`echo $conn | cut -d "@" -f 1`
                celery_service=`echo $conn | cut -d "@" -f 2`
                if [ "$host_service" == "$host" ]; then
                    REBUILD_DOCKER_IMAGE $host $celery_service
                    if ! [ $? -eq 0 ]; then
                        echo "Error: REBUILD_DOCKER_IMAGE failed for $celery_service at $host. Stopping pipeline"
                        exit 1
                    fi
                fi
            done
        fi
    done
}

function RESTART_ENVIRONMENT() {
    for conn in $CELERY_SERVICES; do
        host=`echo $conn | cut -d "@" -f 1`
        celery_service=`echo $conn | cut -d "@" -f 2`
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
