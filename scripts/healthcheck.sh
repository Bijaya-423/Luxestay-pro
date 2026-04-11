#!/bin/bash

set -e

echo ">>> Running Health check ..."

#create APi Gateway v2 payload
cat > /tmp/payload.json << 'EOF'
{
  "version": "2.0",
  "routeKey": "GET /",
  "rawPath": "/",
  "rawQueryString": "",
  "headers": {"host": "localhost"},
  "requestContext": {
    "http": {
      "method": "GET",
      "path": "/",
      "protocol": "HTTP/1.1",
      "sourceIp": "127.0.0.1",
      "userAgent": "Jenkins-HealthCheck"
    }
  },
  "isBase64Encoded": false
}
EOF

#invoke lambda
aws lambda invoke \
    --function-name ${LAMBDA_FUNCTION} \
    --region ${AWS_REGION} \
    --cli-binary-format raw-in-base64-out \
    --payload file:///tmp/payload.json \
    /tmp/lambda_response.json


echo ">>> Lambda response:"
cat /tmp/lambda_response.json


#check status code is 200
STATUS=$(cat /tmp/lambda_response.json | python3 -c \
    "import sys, json; print(json.load(sys.stdin).get('statusCode', 0))")

if [ "$STATUS" = "200" ]; then
    echo ">>> Health check passed..."
else
    echo ">>> Health check failed - Status: ${STATUS}"
    exit 1
fi
