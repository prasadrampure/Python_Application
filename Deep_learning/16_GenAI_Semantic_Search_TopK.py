from sentence_transformers import SentenceTransformer, util   

# Load pretrained Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# knowldge Base
documents = [
    "Python is used for machine learning",
    "Java is used for entrprise application",
    "SQL is used to manage databases",
    "HTML is udes to create web pages",
    "Tensorflow is used for deep learning"
]

# generate document embedding
document_embedding = model.encode(documents,convert_to_tensor=True)

# Accept question
query = input("Enter Your Question : ")

# generate query embedding
query_embedding = model.encode(query,convert_to_tensor=True)

# Calculate similarity
scores = util.cos_sim(query_embedding,document_embedding)[0]

# Find Top 2 matching documents
top_result = scores.topk(2)

print("Top 2 relevent documents")

for index in top_result.indices:
    print(documents[index.item()])