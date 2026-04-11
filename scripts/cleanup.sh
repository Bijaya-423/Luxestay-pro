#!/bin/bash

echo ">>> Cleaning up Docker Images...."

docker rmi ${ECR_REGISTRY}/${ECR_REPO_NAME}:${IMAGE_TAG} 2>/dev/null || true
docker image prune -f 2>/dev/null || true


echo ">>> Cleanup Complete...."


