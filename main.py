from fastapi import FastAPI, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import httpx
from pydantic import BaseModel

# Define the structure of the request and response for clarity
class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

# Initialize the FastAPI app
app = FastAPI()

# Mount the static files, typically React build folder
app.mount("/static", StaticFiles(directory="public"), name="static")

# Define the route for the chatbot API
@app.post("/chat/", response_model=ChatResponse)
async def chat(chat_request: ChatRequest):
    # Replace 'your_chatgpt_api_endpoint' with the actual endpoint of your ChatGPT API
    chatgpt_api_endpoint = "your_chatgpt_api_endpoint"
    # Replace 'your_api_key' with your actual API key for authentication
    headers = {"Authorization": "Bearer your_api_key"}

    try:
        # Send the user's question to the ChatGPT API
        async with httpx.AsyncClient() as client:
            response = await client.post(chatgpt_api_endpoint, json={"prompt": chat_request.question}, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Extract the answer from the response
            data = response.json()
            return ChatResponse(answer=data['choices'][0]['message']['text'])
        else:
            raise HTTPException(status_code=response.status_code, detail="Error while communicating with the ChatGPT API")

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=str(e))

# Define the root route to serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open('public/index.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# Run the application using Uvicorn if the script is executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
