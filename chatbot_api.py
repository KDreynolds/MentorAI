# chatbot_api.py

from typing import Dict
import httpx
from fastapi import HTTPException

# Define a function to interact with the ChatGPT API
async def get_chatbot_response(question: str, api_endpoint: str, api_key: str) -> Dict:
    """
    Send a question to the ChatGPT API and return the response.

    :param question: The question to send to the ChatGPT API.
    :param api_endpoint: The endpoint URL of the ChatGPT API.
    :param api_key: The API key for authenticating with the ChatGPT API.
    :return: A dictionary containing the response from the ChatGPT API.
    """
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        # Send the user's question to the ChatGPT API
        async with httpx.AsyncClient() as client:
            response = await client.post(api_endpoint, json={"prompt": question}, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the answer from the response
            data = response.json()
            return data
        else:
            raise HTTPException(status_code=response.status_code, detail="Error while communicating with the ChatGPT API")

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))

# This file can also include any additional helper functions related to the ChatGPT API if needed.
