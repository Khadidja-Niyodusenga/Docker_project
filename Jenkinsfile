pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub code downloaded successfully!'
            }
        }

        stage('Build') {
            steps {
                sh '/usr/bin/docker build -t student-frontend:latest ./frontend'
            }
        }

        stage('Deploy') {
            steps {
                sh '/usr/bin/docker rm -f student-frontend || true'

                sh '''
                    /usr/bin/docker run -d \
                    --name student-frontend \
                    --restart unless-stopped \
                    -p 8082:80 \
                    student-frontend:latest
                '''
            }
        }
    }
}