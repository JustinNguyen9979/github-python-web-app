pipeline {
    agent any
    stages {
        stage ('Clone') {
            steps {
                git 'https://github.com/huynguyen011097/github-python-web-app.git'
            }
        }
        stage ('Build stage') {
            steps {
                withDockerRegistry(credentialsId: 'docker-hub-2', url: 'https://index.docker.io/v1/') {
                    sh 'docker build -t 997909799/pythonwebapp:V1.1 .'
                    sh 'docker push 997909799/pythonwebapp:V1.1'
                }
            }
        }
    }
}

