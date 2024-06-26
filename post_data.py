import requests
from loguru import logger

# Set up logging
logger.add("logs_info.log", level="INFO", format="{time} - {level} - {message}")

url = "http://127.0.0.1:8000/summarize"
payload = {
    "text": "Artificial intelligence (AI) has become a transformative force in various industries, from healthcare to finance, and even in creative fields like art and music. AI systems can analyze vast amounts of data quickly and accurately, providing insights that were previously unattainable. In healthcare, AI is used to predict patient outcomes, personalize treatment plans, and even assist in surgeries with precision. Financial institutions use AI to detect fraudulent activities, manage risks, and automate trading processes. In the creative sector, AI tools can generate music, create visual art, and even write poetry. As AI continues to evolve, ethical considerations such as privacy, bias, and job displacement must be addressed to ensure that its benefits are realized responsibly."
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

try:
    response_data = response.json()
    logger.info(response_data)
except requests.exceptions.JSONDecodeError:
    logger.info(f"Failed to decode JSON response. Raw response: {response.text}")
