#!/bin/bash

set -e

echo ">>> Logging in to Aws ECR.........."

aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${ECR_REGISTRY}


#${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com

echo ">>> ECR Login Successful"
