sentence = "food was not good"

words = sentence.split()

print("Actual setence is :",sentence)

for index, word in enumerate(words):
    print("TimeStep :",index+1, ":",word)