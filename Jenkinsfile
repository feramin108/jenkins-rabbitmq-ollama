pipeline {
    agent any
    environment {
        RABBITMQ_HOST = "localhost"
        RABBITMQ_PORT = "15672"
        RABBITMQ_USER = "admin"
        RABBITMQ_PASSWORD = "Jre-8u251npp@kazan"
        RABBITMQ_EXCHANGE = "logs_exchange"
        RABBITMQ_ROUTING_KEY = "jenkins_logs"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    def logMessage = "Build stage started at: ${new Date()}"
                    echo logMessage
                    sh """
                    curl -u $RABBITMQ_USER:$RABBITMQ_PASSWORD -X POST "http://$RABBITMQ_HOST:$RABBITMQ_PORT/api/exchanges/%2F/$RABBITMQ_EXCHANGE/publish" \
                        -H "Content-Type: application/json" \
                        -d '{
                            "properties": {},
                            "routing_key": "$RABBITMQ_ROUTING_KEY",
                            "payload": "$logMessage",
                            "payload_encoding": "string"
                        }'
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    def logMessage = "Deploying application..."
                    echo logMessage
                    sh """
                    curl -u $RABBITMQ_USER:$RABBITMQ_PASSWORD -X POST "http://$RABBITMQ_HOST:$RABBITMQ_PORT/api/exchanges/%2F/$RABBITMQ_EXCHANGE/publish" \
                        -H "Content-Type: application/json" \
                        -d '{
                            "properties": {},
                            "routing_key": "$RABBITMQ_ROUTING_KEY",
                            "payload": "$logMessage",
                            "payload_encoding": "string"
                        }'
                    """
                }
            }
        }
    }
}
