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
     ],
     format="json"
)

answer = responce.message.content

print("LLM Responce")
print(answer)

# Convert json string to python dictonary
data = json.loads(answer)

print("Data from dictnory is :",data)

print("Data from Dictonary")

print("Language :",data.get("language"))
print("Type :",data.get("type"))
print("Creator :",data.get("creater"))
