words = ["food", "was", "not", "good"]

hidden_state = "empty memory"

print("Input tokens :",words)

print("Initial hidden state :",hidden_state)

for index,word in enumerate(words):
    print("TimeStep :",index+1)
    print("Current word :",word)
    print("Previous memory :",hidden_state)

    hidden_state = "memory after reading " + " ".join(words[:index + 1]) + ""
    print("Updted memory :",hidden_state)

    print("-"*50)