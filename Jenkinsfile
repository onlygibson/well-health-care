pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Validate Project Files') {
            steps {
                echo 'Validating project structure...'
                sh 'ls -la'
                sh 'test -f backend/Dockerfile'
                sh 'test -f frontend/Dockerfile'
                sh 'test -f docker-compose.yml'
                sh 'test -f backend/main.py'
                sh 'test -f backend/requirements.txt'
            }
        }

        stage('Validate Dockerfiles') {
            steps {
                echo 'Checking Dockerfile contents...'
                sh 'grep -i "FROM" backend/Dockerfile'
                sh 'grep -i "FROM" frontend/Dockerfile'
                sh 'grep -i "CMD" backend/Dockerfile'
                sh 'grep -i "CMD" frontend/Dockerfile'
            }
        }

        stage('Validate Compose File') {
            steps {
                echo 'Checking Docker Compose file exists...'
                sh 'cat docker-compose.yml'
            }
        }
    }

    post {
        success {
            echo 'CI validation completed successfully.'
        }
        failure {
            echo 'CI validation failed.'
        }
    }
}