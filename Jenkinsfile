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
                        bat "docker build -t shayancyan/mlopsa1:${env.BUILD_NUMBER} ."
                        bat "docker push shayancyan/mlopsa1:${env.BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}
