from sentence_transformers import SentenceTransformer   
from sentence_transformers import util

# Load pretrained Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

sentence1 =   "Python is a programing language",
sentence2 = "I support love to play cricket",

embegging1 = model.encode(sentence1,convert_to_tensor=True)
embegging2 = model.encode(sentence2,convert_to_tensor=True)

# Calculate cosine similarity
similarity = util.cos_sim(embegging1,embegging2)

print("Sentence 1:",sentence1)
print("Sentence 2:",sentence2)

print("Cosine Similarity :")
print(similarity.item())