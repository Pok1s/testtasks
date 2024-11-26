pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "flask-app:latest"  
    }
    stages {
        stage('Clone repository') {
            steps {
                git 'https://github.com/Pok1s/testtasks.git' 
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 5001:5001 --name flask-app $DOCKER_IMAGE'
            }
        }
        stage('Test Application') {
            steps {
                sh 'curl -f http://localhost:5001/health || exit 1'
            }
        }
        stage('Clean Up') {
            steps {
                sh 'docker stop flask-app && docker rm flask-app'
            }
        }
    }
}
