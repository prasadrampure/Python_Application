sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1,0,0]

for sentence , label in zip(sentences,labels):
    
    print("Sentence :",sentence)
    print("Label :",label)

    if label == 1:
        print("Meaning Positive Sentiment")
    else:
        print("Meaning Negative Sentiment")
        
    print("----------------------------------")
