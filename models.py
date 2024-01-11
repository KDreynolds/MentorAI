# models.py

from pydantic import BaseModel

# Define the structure of the request and response for clarity
class ChatRequest(BaseModel):
    question: str

class ChatResponse(BaseModel):
    answer: str

# Note: Since the project description does not specify additional models or database interactions,
# the above models are sufficient for the current scope of the project. If the project scope
# expands to include user management, message history, or other features, additional models
# would be required and should be defined here.
