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

# create prompt for LLM
prompt = f"""
Answer the question using only the give context.

Context: {context}

Question: {query}

if the answer is not avalable in context,
say "information not available"
"""

# Send the context and question to ollama(llama)
responce = chat(
    model = "llama3.2:1b",
    messages= [
        {
            "role" : "user",
            "content" : prompt
        }
    ]
)

answer = responce.message.content

print("Marvellous GenAI : RAG Answer :")
print(answer)