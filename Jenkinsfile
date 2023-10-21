pipeline {
    agent any
    stages {
        stage ('Clone stage') {
            steps {
                // echo 'Hello world'
                git credentialsId: 'Repo_Gitlab_PythonWebApp', url: 'https://gitlab.com/justin_nguyen_9979/pythonwebapp.git'
                sh 'git clone https://gitlab.com/justin_nguyen_9979/pythonwebapp.git'
            }
        }
        stage ('Build stage') {
            steps {
                withDockerRegistry(credentialsId: 'Docker-Hub', url: 'https://index.docker.io/v1/') {
                    sh 'docker build -t 997909799/pythonwebapp:V1.0 .'
                    sh 'docker push 997909799/pythonwebapp:V1.0'
                }
            }
        }
    }
}