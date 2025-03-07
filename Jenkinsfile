pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        // Use 'bat' instead of 'sh' on Windows
                        bat "docker build -t your-dockerhub-username/mlopsa1:${env.BUILD_NUMBER} ."
                        bat "docker push your-dockerhub-username/mlopsa1:${env.BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}
