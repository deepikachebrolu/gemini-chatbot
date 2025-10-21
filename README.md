# gemini-chatbot
 Gemini-Chatbot
A simple command-line chatbot built using the google.generativeai SDK and the Gemini 2.5 Flash model.

 Features:
Uses Google's Gemini 2.5 Flash model for fast, conversational AI
Maintains context across messages via chat sessions
Clean CLI interface
Simple, minimal setup

 Requirements:
Python 3.8+
Google Generative AI SDK (google-generativeai)
A valid GEMINI_API_KEY from Google AI Studio

 Installation:
Clone the repository or download the script:
git clone https://github.com/your-username/gemini-chatbot.git
cd gemini-chatbot
Install dependencies:
pip install google-generativeai
Set your API key:
Set your GEMINI_API_KEY as an environment variable:

On Linux/macOS:
export GEMINI_API_KEY="your_api_key_here"
On Windows (Command Prompt):
set GEMINI_API_KEY=your_api_key_here
Or use a .env file (with the help of python-dotenv) if you prefer.

🧠 Usage
Run the chatbot script:

python chatbot.py
You'll see:

🤖 Chatbot: Hello! I'm a Gemini-powered AI. Ask me anything!
🤖 Chatbot: Type 'exit' or 'quit' to end the conversation.

------------------------------
You:
Start chatting! Type exit or quit to leave the session.

🧪 Example
You: What is the capital of Japan?
🤖 Chatbot: The capital of Japan is Tokyo.
❗ Troubleshooting
Error initializing client: Make sure your GEMINI_API_KEY is correctly set and not expired.

Network errors: Check your internet connection and firewall settings.

📄 License
MIT License

🙌 Credits
Powered by Google Generative AI SDK
Built using the Gemini 2.5 Flash model
