from google import genai
# The SDK automatically finds the GEMINI_API_KEY environment variable.

# 1. Initialize the Client
try:
    client = genai.Client()
except Exception as e:
    print(f"Error initializing client: {e}")
    print("Please ensure you have set your GEMINI_API_KEY environment variable.")
    exit()

# 2. Start a Chat Session (to manage conversation history)
# Using 'gemini-2.5-flash' for speed and general chat
chat = client.chats.create(model="gemini-2.5-flash")

print("🤖 Chatbot: Hello! I'm a Gemini-powered AI. Ask me anything!")
print("🤖 Chatbot: Type 'exit' or 'quit' to end the conversation.")
print("-" * 30)

# 3. Main Conversation Loop
while True:
    try:
        user_input = input("You: ")

        if user_input.lower() in ["quit", "exit"]:
            print("🤖 Chatbot: Goodbye! Have a great day.")
            break

        # Send the message and get the multi-turn response
        response = chat.send_message(user_input)

        # Print the model's response
        print(f"🤖 Chatbot: {response.text}")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your network connection or API key.")
        break
