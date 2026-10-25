import chromadb
from sentence_transformers import SentenceTransformer, util 
from ollama import chat  

# Load pretrained Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to existing Chromabd
client = chromadb.PersistentClient(path="./MarvellousDB")

collection = client.get_collection(name="Marvellous_knowledge")

# Accept question
query = input("Enter Your Question : ")

# generate query embedding
query_embedding = model.encode(query,convert_to_tensor=True)

# retrive top 2 relevent results
results = collection.query(query_embeddings=[query_embedding.tolist()], n_results=2)

# Create context from retrived documents
documents = results["documents"][0]

context = "\n".join(documents)

print("Retrived context :")
print(context)
