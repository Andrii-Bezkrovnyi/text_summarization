# FastAPI Text Summarizer

This is a simple FastAPI-based application that provides an API for text summarization. It uses the HuggingFace model to generate summaries of the provided text.


The code consists of three main endpoints:

1. `/`: Contain Root route.
2. `/summarize`: Contain Route for summarizing the text.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Loguru
- Python-dotenv
- Langchain
- Langchain HuggingFace

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Andrii-Bezkrovnyi/text_summarization.git
    ```

2. Navigate to the project directory:

    ```bash
    cd text_summarization
    ```

3.  Create a .env file in the project directory with the following content:

    ```
    HUGGINGFACEHUB_API_TOKEN=YOUR_HUGGINGFACEHUB_API_TOKEN
    ```
   
4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the script for start Fastapi server:

    ```bash
    python main.py
    ```
   or
    
   ```bash
    uvicorn main:app --reload
    ```
6. Run the script for test `/summarize` endpoint:

    ```bash
    python post_data.py  
    ```