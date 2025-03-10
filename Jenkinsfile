pipeline {
    agent any
    environment {
        RABBITMQ_HOST = "http://13.60.117.51:15672/"
        RABBITMQ_QUEUE = "jenkins_logs"
        RABBITMQ_USERNAME = "jenkins"
        RABBITMQ_PASSWORD = "Jre-8u251npp@kazan"
        RABBITMQ_VHOST = "jenkins_vhost"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    def logMessage = "Build stage started at: ${new Date()}"
                    echo logMessage
                    publishRabbitMQ message: logMessage, routingKey: "${RABBITMQ_QUEUE}", exchange: ""
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    def logMessage = "Running security tests..."
                    echo logMessage
                    publishRabbitMQ message: logMessage, routingKey: "${RABBITMQ_QUEUE}", exchange: ""
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def logMessage = "Deploying application to production..."
                    echo logMessage
                    publishRabbitMQ message: logMessage, routingKey: "${RABBITMQ_QUEUE}", exchange: ""
                }
            }
        }
    }
}
