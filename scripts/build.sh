#!/bin/bash

set -e


echo ">>> Staring Docker Build...."
echo "    Image: ${ECR_REGISTRY}/${ECR_REPO_NAME}:${IMAGE_TAG}"


#create or reuse buildx builder
docker buildx create --name lambdabuilder --use 2>/dev/null || \
    docker buildx use lambdabuilder


    # #build and push image
    # docker buildx build \
    # --platform linux/amd64 \
    # --tag ${ECR_REGISTRY}/${ECR_REPO_NAME}:${IMAGE_TAG} \
    # --push \
    # .

docker buildx inspect --bootstrap

#Build linux/amd64 image and push directly to ECR
# --provenance=false prevents OCI manifest that lambda rejects

docker buildx build \
    --platform linux/amd64 \
    --provenance=false \
    -t ${ECR_REGISTRY}/${ECR_REPO_NAME}:${IMAGE_TAG} \
    -t ${ECR_REGISTRY}/${ECR_REPO_NAME}:latest \
    --push \

echo ">>> Build and push Complete"
