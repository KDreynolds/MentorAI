# settings.py

# Define the settings for the ChatGPT API interaction
class Settings:
    # The endpoint URL of the ChatGPT API
    CHATGPT_API_ENDPOINT: str = "your_chatgpt_api_endpoint"
    # The API key for authenticating with the ChatGPT API
    CHATGPT_API_KEY: str = "your_api_key"
    # The host for the FastAPI application
    HOST: str = "0.0.0.0"
    # The port for the FastAPI application
    PORT: int = 8000

# Instantiate the Settings class to access the settings throughout the application
settings = Settings()
