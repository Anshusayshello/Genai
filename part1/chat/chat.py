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

#adding memory layer (without using prompt template)
from langchain_core.messages import AIMessage, SystemMessage , HumanMessage

print("chose your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode ")
print("press 3 for sad mode")

choice = int(input("tell your response :- "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."


messages = [
    SystemMessage(content=mode)
]

print("----------------- welcome type 0 to exit the application-----------------")
while True:
    
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot :",response.content)

print(messages)

