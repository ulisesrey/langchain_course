from langchain_ollama import ChatOllama 
from dotenv import load_dotenv

load_dotenv()

llm = ChatOllama(model="mistral", temperature=0.0) 
llm.invoke("Hello, world!")
print("LLM response:", llm.invoke("Hello, world!"))
# This is a simple test to check if the LLM is working correctly.
# If the LLM is working correctly, it should return a response without any errors.
# If you see an error, check your environment variables and make sure the model is available.
if __name__ == "__main__":
    print("LLM test completed successfully.")
