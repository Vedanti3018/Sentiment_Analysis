from langchain_ollama import OllamaLLM
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from fastapi import FastAPI
import random
import json
import time
import uvicorn
from pydantic import BaseModel


app = FastAPI()


class RequestModel(BaseModel):
    text: str


class ResponseModel(BaseModel):
    statusCode: int
    score: float
    sentiment: str


@app.post("/api/sentiment")
async def generate_sentiment(request: RequestModel):
    start_time = time.time()  # Start time
    texts = request.text
    try:
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

        llm_olla = OllamaLLM(
            model="mistral-nemo",
            callback_manager=callback_manager,
            verbose=True,
            temperature=0,
            top_p=1
        )

        prompt_template = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request.

    #### Instruction:
    You are an advanced AI assistant named Senty. Your task is to perform sentiment analysis on input text. Carefully consider all parts of the text, including words, phrases, hashtags, mentions, humor, sarcasm, and any shifts in tone. 
    Consider the following:
    - Carefully consider all parts of the text, including words, phrases, humor, sarcasm, and any shifts in tone.
    - If the text contains sarcasm or humor, identify the underlying sentiment behind the language.
    - If humor, sarcasm, or irony is detected, analyze how they influence the sentiment.
    - If the text consists only of hashtags, mentions, or URLs, return "neutral".

    Always provide the same sentiment result for the same text input, ensuring consistency across multiple runs.

    I need you to classify each text you receive and provide your analysis using the following JSON schema:
    {{
        "overall_sentiment": {{
          "type": "string",
          "description": "The overall sentiment category. One of 'Strongly Positive', 'Positive', 'Neutral', 'Negative', 'Strongly Negative'.",
          "required": true
        }},
        "overall_score": {{
          "type": "number",
          "description": "The overall sentiment score, ranges from 0 to 1.",
          "required": true,
          "format": ".2f"
        }}
    }}
    Always respond with a valid JSON object adhering to this schema.
    Do not include any other text or messages in your response.
    Exclude markdown.

    ### Input:
    {text_prompt}


    ### Response:
    """

        prompt = prompt_template.format(text_prompt=texts)

        # Debugging: Print prompt before sending to LLM
        print("Sending prompt to LLM:", prompt)

        response = llm_olla.invoke(prompt)

        # Debugging: Print raw response
        print("Raw LLM Response:", response)

        try:
            response_json = json.loads(response)
        except json.JSONDecodeError as e:
            print("JSON Decode Error:", str(e))
            return {"statusCode": 500, "message": "Invalid response from LLM"}

        senti = response_json["overall_sentiment"]
        if senti == "Strongly Positive":
            score = random.uniform(0.8, 0.95)
        elif senti == "Positive":
            score = random.uniform(0.5, 0.8)
        elif senti == "Neutral":
            score = random.uniform(0.35, 0.5)
        elif senti == "Negative":
            score = random.uniform(0.15, 0.35)
        else:
            score = random.uniform(0, 0.15)


        print(f"final_score: {score:.2f}")
        result_body = round(score, 4) * 100

        result = ResponseModel(statusCode=200, score=result_body, sentiment=senti)
        end_time = time.time()
        processing_time = end_time - start_time
        print(f"Sentiment time: {processing_time:.2f} seconds")

        return result

    except Exception as e:
        print("Error:", str(e))
        return {"statusCode": 500, "message": "Error during sentiment analysis"}


# Run the FastAPI app when the script is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
