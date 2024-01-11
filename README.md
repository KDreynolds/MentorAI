# MentorAI

MentorAI is a web-based chatbot application designed to simulate a senior developer mentor. It leverages a custom ChatGPT profile to provide users with insightful and helpful responses to their programming-related questions.

## Features

- Interactive chat interface to communicate with the ChatGPT-based mentor.
- Real-time response display from the ChatGPT API.
- Built with FastAPI for the backend and React for the frontend.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mentorai.git
cd mentorai
```

2. Install backend dependencies:

```bash
pip install -r requirements.txt
```

3. Install frontend dependencies:

```bash
cd path/to/your/frontend/directory # Replace with your actual frontend directory path
npm install
```

## Usage

To run the backend server:

```bash
uvicorn main:app --reload
```

To start the frontend React application:

```bash
npm start
```

The application will be available at `http://localhost:3000` by default.

## Configuration

Before running the application, ensure you have set up the following:

- In `settings.py`, replace `your_chatgpt_api_endpoint` and `your_api_key` with your actual ChatGPT API endpoint and API key.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the GPT-3 API.
- FastAPI and React communities for their excellent documentation and resources.

