pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from Git
                checkout scm
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                script {
                    // Use Docker Hub credentials stored in Jenkins
                    docker.withRegistry('', 'dockerhub-credentials') {
                        // 'dockerhub-credentials' is the ID you gave your Docker Hub credentials
                        
                        // Build the Docker image (using the Dockerfile in the repo root)
                        sh "docker build -t your-dockerhub-username/mlopsa1:${env.BUILD_NUMBER} ."
                        
                        // Push the Docker image
                        sh "docker push your-dockerhub-username/mlopsa1:${env.BUILD_NUMBER}"
                    }
                }
            }
        }
    }
}
