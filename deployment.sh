#!/bin/bash
SSH_USER='alex'
SRC_DIRECTORY='/home/alex/scraping-infra'
source .env
read -p "Enter the branch you want to set " CURRENT_BRANCH

function PULL_REPO() {
    SSH_CMD="cd $SRC_DIRECTORY && git checkout $CURRENT_BRANCH && git pull"
    echo "Pulling repo at $SSH_USER@$1"
    ssh "$SSH_USER"@$1 "$SSH_CMD"
}

function PIP_INSTALL() {
    scp ./requirements.txt $SSH_USER@$1:$SRC_DIRECTORY/requirements.txt SSH_CMD="cd $SRC_DIRECTORY && /usr/local/bin/docker build -t  scraping_infra -f compose/Dockerfile . "
    ssh "$SSH_USER"@$1 "$SSH_CMD"
    echo "Updated libraries successfully."
}

function RESTART_CONTAINER() {
    SSH_CMD="cd $SRC_DIRECTORY && docker compose -f docker-compose.yml restart $2"
    ssh "$SSH_USER"@"$1" "$SSH_CMD"
}


function UPDATE_CODE() {
    host=`echo $CELERY_SERVICES | cut -d "@" -f 1`
    echo $host
    echo "Get requirements from $SSH_USER@$host:$SRC_DIRECTORY"
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

    for conn in $CELERY_SERVICES; do
        host=`echo $conn | cut -d "@" -f 1`
        PULL_REPO $host
        if [ "$PIP_FLAG" -eq 1 ]; then
            PIP_INSTALL $host
            if ! [ $? -eq 0 ]; then
                echo "Error: PIP_INSTALL failed for $host. Stopping pipeline"
                exit 1
            fi
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