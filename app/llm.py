import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_llm(system_prompt: str, user_prompt: str):

    try:

        prompt = f"""
{system_prompt}

---

{user_prompt}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if not response.text:
            raise Exception("Empty response")

        return response.text

    except Exception as e:
        print(f"[LLM ERROR] {e}")
        raise