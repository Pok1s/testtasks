pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "flask-app:latest"
    }
    stages {
        stage('Debug Git') {
            steps {
                sh 'git --version'
                sh 'git ls-remote https://github.com/Pok1s/testtasks'
            }
        }
        stage('Clone repository') {
            steps {
                sh '''
                    git clone https://github.com/Pok1s/testtasks
                    cd testtasks
                    ls -la
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh '''
                    cd testtasks
                    docker build -t ${DOCKER_IMAGE} .
                '''
            }
        }
        stage('Run Docker Container') {
            steps {
                sh '''
                    docker run -d -p 5001:5001 --name flask-app ${DOCKER_IMAGE}
                '''
            }
        }
        stage('Test Application') {
            steps {
                script {
                    def testResult = sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:5001/health', returnStdout: true).trim()
                    if (testResult != '200') {
                        error "Application health check failed with HTTP status code: ${testResult}"
                    }
                }
            }
        }
        stage('Clean Up') {
            steps {
                sh '''
                    docker stop flask-app || true
                    docker rm flask-app || true
                '''
            }
        }
    }
    post {
        always {
            sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                rm -rf testtasks
            '''
        }
    }
}
