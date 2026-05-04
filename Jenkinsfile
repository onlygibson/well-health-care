pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Validate Files') {
            steps {
                echo 'Validating project structure...'
                sh 'ls -la'
                sh 'test -f backend/Dockerfile'
                sh 'test -f frontend/Dockerfile'
                sh 'test -f docker-compose.yml'
            }
        }

        stage('Build Backend Image') {
            steps {
                echo 'Building backend Docker image...'
                sh 'docker build -t well-health-backend:1.0 ./backend'
            }
        }

        stage('Build Frontend Image') {
            steps {
                echo 'Building frontend Docker image...'
                sh 'docker build -t well-health-frontend:1.0 ./frontend'
            }
        }

        stage('List Docker Images') {
            steps {
                echo 'Confirming Docker images were created...'
                sh 'docker images | grep well-health'
            }
        }
    }
}