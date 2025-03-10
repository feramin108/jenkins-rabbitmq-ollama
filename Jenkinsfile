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
                    rabbitMQPublisher(
                        message: logMessage,
                        routingKey: "${RABBITMQ_QUEUE}",
                        exchange: "",
                        host: "${RABBITMQ_HOST}",
                        username: "${RABBITMQ_USERNAME}",
                        password: "${RABBITMQ_PASSWORD}"
                    )
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def logMessage = "Deploying application..."
                    echo logMessage
                    rabbitMQPublisher(
                        message: logMessage,
                        routingKey: "${RABBITMQ_QUEUE}",
                        exchange: "",
                        host: "${RABBITMQ_HOST}",
                        username: "${RABBITMQ_USERNAME}",
                        password: "${RABBITMQ_PASSWORD}"
                    )
                }
            }
        }
    }
}