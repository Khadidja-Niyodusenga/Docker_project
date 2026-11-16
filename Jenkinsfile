
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Latest GitHub code downloaded!'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t student-frontend:latest ./frontend'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker rm -f student-frontend || true'

                sh '''
                    docker run -d \
                    --name student-frontend \
                    --restart unless-stopped \
                    -p 8082:80 \
                    student-frontend:latest
                '''
            }
        }
    }
}
