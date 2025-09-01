pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yojyna:${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Trivy Scan (Docker Image)') {
            steps {
                sh '''
                  echo "Scanning Docker image for vulnerabilities..."
                  trivy image --exit-code 1 --severity HIGH,CRITICAL $DOCKER_IMAGE
                '''
            }
        }

        stage('Trivy Scan (Project Files)') {
            steps {
                sh '''
                  echo "Scanning source code for vulnerabilities..."
                  trivy fs --exit-code 1 --severity HIGH,CRITICAL .
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}