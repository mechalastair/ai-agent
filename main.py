import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def main():
    print("Hello from ai-agent!")
    if len(sys.argv) < 2:
        raise TypeError("User must provide input text")
    user_prompt = sys.argv[1]
    verbose = "--verbose" in sys.argv
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001", 
        contents = messages,
        )
    if verbose:
        print(f"User prompt: {user_prompt}") 
    print(response.text)
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
