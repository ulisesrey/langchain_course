import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SOME CODE IS ACTUALLY ON PROMOT.PY

if __name__ == "__main__":
    print("Hello LangChain.")
    API_KEY = os.environ["OPENAI_API_KEY"]
    print(API_KEY)
    