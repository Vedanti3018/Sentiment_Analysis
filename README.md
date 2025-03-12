# Sentiment Analysis API with Mistral-Nemo

![Workflow Diagram](https://via.placeholder.com/800x400.png?text=Sentiment+Analysis+Workflow)
*Example workflow diagram - Replace with your actual image*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green.svg)](https://fastapi.tiangolo.com/)

A production-ready sentiment analysis API using Mistral-Nemo model via Ollama, deployed on Runpod GPU instances.

## Features

- 🚀 Real-time sentiment scoring (0-100 scale)
- 🎯 Five-tier sentiment classification
- 😂 Sarcasm & humor detection
- 🔄 Consistent results for same inputs
- 📦 Docker-ready configuration
- 🌐 REST API endpoint

## Table of Contents

- [Installation](#installation)
- [API Usage](#api-usage)
- [Runpod Deployment](#runpod-deployment)
- [Gradio Interface](#gradio-interface)
- [Examples](#examples)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
# Clone repository
git clone https://github.com/yourusername/sentiment-analysis-api.git
cd sentiment-analysis-api

# Install dependencies
pip install -r requirements.txt

# Start Ollama service (requires GPU)
ollama serve
```

## API Usage

### Python Client

```python
import requests

API_ENDPOINT = "http://localhost:8000/api/sentiment"

def analyze_sentiment(text):
    payload = {"text": text}
    response = requests.post(API_ENDPOINT, json=payload)
    return response.json()

# Example usage
print(analyze_sentiment("This product exceeded all my expectations! 😍"))
```

### cURL

```bash
curl -X POST "http://localhost:8000/api/sentiment" \
-H "Content-Type: application/json" \
-d '{"text": "The service was slower than a snail racing through peanut butter 🐌"}'
```

## Runpod Deployment

![Runpod Setup](https://via.placeholder.com/600x300.png?text=Runpod+GPU+Setup)
*Runpod configuration example - Replace with actual screenshot*

1. Create GPU instance (NVIDIA A100 recommended)
2. Connect via SSH and setup environment:

```bash
# Install system dependencies
sudo apt-get update && sudo apt-get install -y python3-pip

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull mistral-nemo

# Start API
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1
```

3. Configure network security rules to allow port 8000

## Gradio Interface

![Gradio Demo](https://via.placeholder.com/600x300.png?text=Gradio+Interface+Preview)
*Interactive demo preview - Replace with actual screenshot*



## Examples

### Sample Request
```json
{
  "text": "Prom night! We had a time! Happy birthday Queen!"
}
```

### Sample Response
```json
{
  "statusCode": 200,
  "score": 62.4,
  "sentiment":Positive
}
```

### Interpretation Guide
| Score Range | Sentiment          |
|-------------|--------------------|
| 80-100      | Strongly Positive  |
| 50-80       | Positive           |
| 35-50       | Neutral            |
| 15-35       | Negative           |
| 0-15       | Strongly Negative  |

## Model Details

### Prompt Template
```python
"""
You are an advanced AI assistant named Senty. Your task is to perform sentiment analysis on input text...
"""
```

### Configuration
| Parameter          | Value     |
|--------------------|-----------|
| Model              | mistral-nemo |
| Temperature        | 0         |
| Top-p              | 1         |
| Max Tokens         | 512       |
| Response Format    | JSON      |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Note**: Replace all placeholder images (via.placeholder.com links) with your actual screenshots and diagrams. Consider adding:

1. Architecture diagram
2. Performance metrics
3. Example outputs with different sentiment types
4. Deployment workflow visualization
