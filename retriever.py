from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Load knowledge base
with open("data/knowledge_base.txt", "r", encoding="utf-8") as file:
    documents = [
        line.strip()
        for line in file
        if line.strip()
    ]


# Create embeddings
embeddings = model.encode(documents)

# Convert to NumPy array
embeddings = np.array(embeddings).astype("float32")


# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings to FAISS
index.add(embeddings)


def retrieve_evidence(query, top_k=3):

    # Convert query into embedding
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for i in indices[0]:
        if i < len(documents):
            results.append(documents[i])

    return results


# Test retrieval
if __name__ == "__main__":

    question = input("Enter your question: ")

    evidence = retrieve_evidence(question)

    print("\nRetrieved Evidence:")

    for i, document in enumerate(evidence, 1):
        print(f"\n{i}. {document}")