import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from the .env file
load_dotenv()

# Initialize the Gemini model via LangChain
# Note: Gemini models use 'temperature' instead of 'temperature=0.9' directly if desired,
# but 0.7 to 1.0 works great for creative tasks like poems.
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0.9 ,
     api_key=os.environ.get("Gemini")
)

# Invoke the model with your prompt
response = model.invoke("write a poem on AI")

# Print the text content of the response
print(response.content)
