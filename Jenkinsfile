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
        stage('Docker Diagnosis') {
            steps {
                sh '''
                    echo "=== DOCKER VERSION ==="
                    docker --version

                    echo "=== DOCKER CONNECTION ==="
                    docker ps
                '''
            }
        }

        stage('Build Backend') {
            steps {
                sh 'docker build -t student-backend:1.0 ./backend'
            }
        }

        stage('Build Frontend') {
            steps {
                sh 'docker build -t student-frontend:1.0 ./frontend'
            }
        }

       

stage('Deploy') {
    steps {
        sh '''
            echo "=== CREATE NETWORK ==="
            docker network inspect student-network >/dev/null 2>&1 || \
                docker network create student-network

            echo "=== REMOVE OLD CONTAINERS ==="
            docker rm -f student-frontend student-backend backend || true

            echo "=== START BACKEND ==="
            docker run -d \
                --name backend \
                --restart unless-stopped \
                --network student-network \
                student-backend:1.0

            echo "=== START FRONTEND ==="
            docker run -d \
                --name student-frontend \
                --restart unless-stopped \
                --network student-network \
                -p 8085:80 \
                student-frontend:1.0
        '''
    }
}



        stage('Verify') {
            steps {
                sh '''
                    echo "=== RUNNING CONTAINERS ==="
                    docker ps

                    echo "=== NETWORK ==="
                    docker network inspect student-network
                '''
            }
        }
    }
}
