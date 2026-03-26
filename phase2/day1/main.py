from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

#settings 
temperature = 0.7
max_tokens=400

print("choose model")
print("1: gemini flash")
print("2: gemini pro")
choice = input("enter choice:")

if choice == "1":
    model = ChatGoogleGenerativeAI(model= "gemini-2.5-flash-lite", temperature=temperature, max_output_tokens=max_tokens)

elif choice =="2":
    model = ChatGoogleGenerativeAI(model = "gemini-2.5-pro",temperature=temperature, max_output_tokens=max_tokens)

else:
    print("Invalid choice")
    exit()

prompt = input("\nEnter your prompt: ")
response = model.invoke(prompt)
print("\nResponse:\n")
print(response.content)