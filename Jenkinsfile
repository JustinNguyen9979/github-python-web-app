// pipeline {
//     agent any
//     environment {
//         DOCKER_IMAGE = 'docker:latest'
//     }
//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('Install Docker') {
//             steps {
//                 script {
//                     // Start a Docker container to install Docker (DinD approach)
//                     def dockerInstallCmd = """
//                         docker run --rm --privileged --name jenkins-docker \
//                             -d -p 2375:2375 -v /var/run/docker.sock:/var/run/docker.sock \
//                             -v /usr/bin/docker:/usr/bin/docker $DOCKER_IMAGE
//                     """
//                     sh dockerInstallCmd
//                 }
//             }
//         }
//         stage('Test Docker') {
//             steps {
//                 script {
//                     // Test Docker installation
//                     sh 'docker --version'
//                 }
//             }
//         }
//         stage ('Clone') {
//             steps {
//                 git 'https://github.com/huynguyen011097/github-python-web-app.git'
//             }
//         }
//         stage ('Build') {
//             steps {
//                 withDockerRegistry(credentialsId: 'docker-hub-2', url: 'https://index.docker.io/v1/') {
//                     sh 'docker build -t 997909799/pythonwebapp:V1.1 .'
//                     sh 'docker push 997909799/pythonwebapp:V1.1'
//                 }
//             }
//         }
//     }
//     post {
//         cleanup {
//             // Clean up the Docker container used for installing Docker
//             script {
//                 sh 'docker stop jenkins-docker'
//             }
//         }
//     }

// }

pipeline {
    agent none
    stages {
        stage('Prepare Docker Image') {
            steps {
                script {
                    // Đảm bảo rằng Docker Daemon đã được kích hoạt
                    def dockerImage = docker.image('docker:dind')
                    dockerImage.inside('-v /var/run/docker.sock:/var/run/docker.sock') {
                        sh 'echo "Docker Daemon is running"'
                    }
                }
            }
        }
        stage('Build and Test') {
            agent {
                docker {
                    // Chọn hình ảnh Docker mà bạn muốn sử dụng làm agent
                    image 'your_custom_docker_image:tag'
                    args '-v /var/run/docker.sock:/var/run/docker.sock'
                }
            }
            steps {
                // Thực hiện các bước xây dựng và kiểm tra ứng dụng trong container Docker
                sh 'docker --version'
                sh 'your_build_and_test_commands_here'
            }
        }
        // Add more stages for your deployment or other tasks
    }
}
