from ollama import chat
import json

# Prompt for LLM
prompt = """Give Me the information about pytohn programming language.
Return the result as json with these keys:
language
type
creater
"""

# execute LLM
responce = chat(
    model = "llama3.2:1b",
     messages=[
        {
        "role" : "user",
        "content" : prompt
        }
     ]
)

answer = responce.message.content

print("LLM Responce")
print(answer)
