# Jenkins + RabbitMQ + Ollama AI

## Overview
This project integrates **Jenkins**, **RabbitMQ**, and **Ollama AI** to analyze CI/CD pipeline logs for security vulnerabilities.

## Components
- **Jenkins**: Fetches logs and sends them to RabbitMQ.
- **RabbitMQ**: Message broker to store logs.
- **Python Consumer**: Listens to logs, processes them, and analyzes them using **Llama3 AI (Ollama)**.
- **Web UI (Future Work)**: Displays security insights.

## Setup

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
