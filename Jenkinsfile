pipeline {
    agent any
    environment {
        RABBITMQ_QUEUE = "jenkins_logs"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    def logMessage = "Build stage started at: ${new Date()}"
                    echo logMessage
                    rabbitMQPublisher(
                        routingKey: "${RABBITMQ_QUEUE}",
                        exchange: ""
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
                        routingKey: "${RABBITMQ_QUEUE}",
                        exchange: ""
                    )
                }
            }
        }
    }
}
