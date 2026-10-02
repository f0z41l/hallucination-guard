from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(answer, evidence):

    answer_embedding = model.encode([answer])
    evidence_embeddings = model.encode(evidence)

    scores = cosine_similarity(
        answer_embedding,
        evidence_embeddings
    )[0]

    return scores


if __name__ == "__main__":

    answer = input("Enter generated answer: ")

    evidence = [
        "France is a country in Western Europe. The capital of France is Paris.",
        "The Eiffel Tower is located in Paris, France. It was completed in 1889.",
        "The Earth is the third planet from the Sun."
    ]

    scores = calculate_similarity(answer, evidence)

    print("\nSimilarity Scores:")

    for i, score in enumerate(scores, 1):
        print(f"Evidence {i}: {score:.4f}")