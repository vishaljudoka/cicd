pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "yojyna:${env.BUILD_NUMBER}"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                   python3 -m venv venv
                   source venv/bin/activate
                   pip install --upgrade pip
                   pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                   source venv/bin/activate
                   pytest tests/
                '''
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
