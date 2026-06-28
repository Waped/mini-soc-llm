from parser import load_alert
from rag import load_knowledge
from llm import ask_llm
from prompts import SYSTEM_PROMPT, build_user_prompt
import json

def main():

    alert = load_alert("alerts/alert1.json")

    context = load_knowledge()

    user_prompt = build_user_prompt(alert, context)

    result = ask_llm(SYSTEM_PROMPT, user_prompt)

    print("\n=== SOC ANALYSIS ===\n")
    print(result)

if __name__ == "__main__":
    main()