import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

prompt = None
verbose = False
if len(sys.argv) > 1:
    prompt = sys.argv[1]
    if len(sys.argv) >= 3:
        if sys.argv[2] == "--verbose":
            verbose = True

elif len(sys.argv)==1:
    #return error
    raise Exception("no argument provided")

def main():
    response = client.models.generate_content(model="gemini-2.0-flash-001",contents=prompt)
    if verbose:
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(response.text)
    


if __name__ == "__main__":
    main()
