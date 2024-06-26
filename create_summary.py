import os

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from loguru import logger

# Налаштування логування
logger.add("logs_info.log", level="INFO", format="{time} - {level} - {message}")

load_dotenv()

# Load environment variables from .env
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if not HUGGINGFACEHUB_API_TOKEN:
    raise ValueError("Please set the HUGGINGFACEHUB_API_TOKEN environment variable")


def generate_summary(text: str) -> str:
    """
    Generate a summary of the provided text using a HuggingFace model.

    This function uses the HuggingFaceEndpoint from the langchain_huggingface
    library to generate a summary of the input text. It constructs a prompt
    using the PromptTemplate and processes the text through the HuggingFace
    model endpoint.

    Args:
        text (str): The text to be summarized.

    Returns:
        str: The generated summary of the input text.

    Raises:
        ValueError: If the HuggingFace API token is not set in the environment variables.
    """
    hub_llm = HuggingFaceEndpoint(
        repo_id='gpt2',
        huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
        temperature=0.9,
        model_kwargs={'max_length': 150}
    )

    prompt = PromptTemplate(
        input_variables=["text"],
        template="Make summarization of the following text: {text}"
    )

    # Use chaining to process the summarization
    hub_chain = prompt | hub_llm

    # Generate the summary
    summary = hub_chain.summarize(text)

    return summary
