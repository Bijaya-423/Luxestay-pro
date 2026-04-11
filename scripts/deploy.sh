#!/bin/bash

set -e

echo ">>> Deploying to Lambda....."
echo "    Function : ${LAMBDA_FUNCTION}"
echo "    Image    : ${ECR_REGISTRY}/${ECR_REPO_NAME}:${IMAGE_TAG}"


#Update Lambda with new image
aws lambda update-function-code \
    --function-name ${LAMBDA_FUNCTION} \
    --image-uri ${ECR_REGISTRY}/${ECR_REPO_NAME}:${IMAGE_TAG} \
    --region ${AWS_REGION}

echo ">>> Waiting for lambda update to complete..."

#wait until lambda is fully updated
aws lambda wait function-updated \
    --function-name ${LAMBDA_FUNCTION} \
    --region ${AWS_REGION}


echo ">>> Lambda deployment complete"

