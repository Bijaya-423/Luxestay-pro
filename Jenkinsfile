pipeline {
    agent any

    environment {
        AWS_REGION            = credentials('AWS_REGION')
        ECR_REGISTRY          = credentials('ECR_REGISTRY')
        ECR_REPO_NAME         = 'ifahms'
        IMAGE_TAG             = "${env.BUILD_NUMBER}"
        LAMBDA_FUNCTION       = credentials('LAMBDA_FUNCTION_NAME')
        AWS_ACCESS_KEY_ID     = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timeout(time: 20, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Bijaya-423/Luxestay-pro.git'
            }
        }

        stage('ECR Login') {
            steps {
                sh 'chmod +x scripts/ecr-login.sh && bash scripts/ecr-login.sh'
            }
        }

        stage('Build and Push to ECR') {
            steps {
                sh 'chmod +x scripts/build.sh && bash scripts/build.sh'
            }
        }

        stage('Deploy to Lambda') {
            steps {
                sh 'chmod +x scripts/deploy.sh && bash scripts/deploy.sh'
            }
        }

        stage('Health Check') {
            steps {
                sh 'chmod +x scripts/healthcheck.sh && bash scripts/healthcheck.sh'
            }
        }



    }
    post {
        success {
            echo "DEPLOYMENT SUCCESSFUL - Build #${env.BUILD_NUMBER}"
        }
        failure {
            echo "DEPLOYMENT FAILED - Build #${env.BUILD_NUMBER}"
        }
        always {
            sh 'chmod +x scripts/cleanup.sh && bash scripts/cleanup.sh'
        }
    }

}

