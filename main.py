import uvicorn
from fastapi import FastAPI, HTTPException, Request
from loguru import logger

from create_summary import generate_summary

app = FastAPI()

# Set up logging
logger.add("logs_info.log", level="INFO", format="{time} - {level} - {message}")


@app.get("/")
async def root():
    return {"message": "Welcome to the summarization API"}


@app.post("/summarize")
async def summarize_text(request: Request):
    data = await request.json()
    text_to_summarize = data.get('text')

    if not text_to_summarize:
        raise HTTPException(status_code=400, detail="Text is required for summarization")

    try:
        summary = generate_summary(text_to_summarize)
        return {"summary": summary}
    except Exception as err:
        logger.error(f"Error during summarization: {str(err)}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(err))


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
