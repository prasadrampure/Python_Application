from ollama import chat

# Select the local LLM
Model = "llama3.2:1b"

# define prompt

prompts = [
    "Explain recursion",

    "Explain recursion in python in 3 simple points",

    """You are experienced python teacher.
    Explain recursion for begginer.
    Give one simple example.""",

    """Convert progrmming languages to uppercase.
    Example 1:
    Input : python
    Output: PYTHON
    
    Example 2:
    Input : java
    Output: JAVA

    Input: javascript
    Output:"""
]

# Execute every prompt
for index, prompt in enumerate(prompts, start=1):
    print("-"*50)
    print("Prompt number :",index)
    print("Input Prompt :",prompt)

    responce = chat(
        model = Model,
        messages=[
            {
            "role" : "user",
            "content" : prompt
            }
        ]
    )

    print("\nResponce from  LLM is :")
    print(responce.message.content)