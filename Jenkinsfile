// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 echo 'GitHub code downloaded successfully!'
//             }
//         }

//         stage('Docker Diagnosis') {
//     steps {
//         sh '''
//             echo "=== PIPELINE HOSTNAME ==="
//             hostname

//             echo "=== PROCESS INFORMATION ==="
//             cat /proc/1/cgroup

//             echo "=== MOUNT INFORMATION ==="
//             grep -E "docker.sock|/var/jenkins_home" /proc/self/mountinfo || true

//             echo "=== JENKINS VARIABLES ==="
//             env | grep -E 'JENKINS|NODE|WORKSPACE|EXECUTOR' || true
//         '''
//     }
// }

//         stage('Build') {
//             steps {
//                 sh '/usr/bin/docker build -t student-frontend:latest ./frontend'
//             }
//         }

//         stage('Deploy') {
//             steps {
//                 sh '/usr/bin/docker rm -f student-frontend || true'

//                 sh '''
//                     /usr/bin/docker run -d \
//                     --name student-frontend \
//                     --restart unless-stopped \
//                     -p 8082:80 \
//                     student-frontend:latest
//                 '''
//             }
//         }
//     }
// }



pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'GitHub code downloaded successfully!'
            }
        }

        stage('Docker Diagnosis') {
            steps {
                sh '''
                    echo "=== DOCKER VERSION ==="
                    docker --version

                    echo "=== DOCKER COMPOSE VERSION ==="
                    docker compose version
                '''
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker rm -f student-frontend student-backend || true
                    docker compose up -d
                '''
            }
        }

        stage('Verify') {
            steps {
                sh '''
                    echo "=== RUNNING CONTAINERS ==="
                    docker compose ps

                    echo "=== ALL DOCKER CONTAINERS ==="
                    docker ps
                '''
            }
        }
    }
}