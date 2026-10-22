from sentence_transformers import SentenceTransformer   

# Load pretrained Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "Python is a programing language",
    "Python is used for data science",
    "I support indian cricket team"
]

embeggings = model.encode(sentences)

# Display sentence embeddings
for index, embegging in enumerate(embeggings):
    print("-"*50)
    print("Sentence :",sentences[index])

    print("Embedding :")
    print(embegging[:10])

    print("Total dimention :",len(embegging))