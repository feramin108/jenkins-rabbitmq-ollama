import pika
import ollama

# RabbitMQ Connection Details
RABBITMQ_HOST = "http://13.60.117.51:15672/"
QUEUE_NAME = "jenkins_logs"

def analyze_log_with_ollama(log_message):
    """Send Jenkins logs to Llama3 for security analysis."""
    prompt = f"""
    Analyze the following CI/CD log for security vulnerabilities:
    
    Log:
    {log_message}
    
    Identify any risks and provide recommended fixes.
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]

def callback(ch, method, properties, body):
    """Process incoming RabbitMQ messages."""
    log_message = body.decode("utf-8")
    print(f"\n📥 Received Log: {log_message}")

    # Analyze with Llama3
    analysis_result = analyze_log_with_ollama(log_message)
    
    # Print Security Analysis
    print("\n🔍 Security Analysis by Llama3:")
    print(analysis_result)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

# Consume messages
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback, auto_ack=True)

print("📡 Listening for Jenkins logs on RabbitMQ...")
channel.start_consuming()
