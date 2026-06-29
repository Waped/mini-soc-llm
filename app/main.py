from app.parser import load_alert
from app.rag import load_knowledge
from app.llm import ask_llm
from app.prompts import SYSTEM_PROMPT, build_user_prompt
from app.utils import retry, fallback_response
import json

def main():

    alert = load_alert("alerts/alert1.json")

    context = load_knowledge()

    user_prompt = build_user_prompt(alert, context)

    try:

        result = retry(lambda: ask_llm(SYSTEM_PROMPT, user_prompt))

        parsed = json.loads(result)

    except Exception as e:

        print("\n LLM failed, using fallback SOC response")

        parsed = fallback_response()

    print("\n=== SOC INCIDENT REPORT ===\n")
    print(json.dumps(parsed, indent=2))

if __name__ == "__main__":
    main()