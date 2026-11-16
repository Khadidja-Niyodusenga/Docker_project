pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'GitHub code downloaded successfully!'
            }
        }

        stage('Docker Diagnosis') {
    steps {
        sh '''
            echo "=== USER ==="
            whoami

            echo "=== HOSTNAME ==="
            hostname

            echo "=== PATH ==="
            echo $PATH

            echo "=== DOCKER FILE ==="
            ls -l /usr/bin/docker || true

            echo "=== DOCKER COMMAND ==="
            command -v docker || true

            echo "=== DOCKER VERSION ==="
            docker --version || true

            echo "=== DOCKER SOCKET ==="
            ls -l /var/run/docker.sock || true
        '''
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