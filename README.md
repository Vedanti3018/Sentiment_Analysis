# Sentiment Analysis API with Mistral-Nemo

![Sentiment Analysis](https://miro.medium.com/v2/resize:fit:626/0*pfvAPHKzpyFiYO3U.jpg)


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
- [Examples](#examples)
- [Model Details](#model-details)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
# Clone repository
 git clone https://github.com/Vedanti3018/Sentiment_Analysis.git
cd Sentiment_Analysis

# Install dependencies
pip install -r requirements.txt

# Start Ollama service (requires GPU)
ollama serve
ollama pull mistral-nemo
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
  "sentiment":"Positive"
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


## License

Distributed under the MIT License. See `LICENSE` for more information.

---


