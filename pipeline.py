import ollama
from retriever import retrieve_evidence
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from nli import classifier
from verifier import calculate_confidence


# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_answer(question):
    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]


def calculate_similarity(answer, evidence):

    answer_embedding = embedding_model.encode([answer])
    evidence_embeddings = embedding_model.encode(evidence)

    scores = cosine_similarity(
        answer_embedding,
        evidence_embeddings
    )[0]

    # Use the most relevant evidence
    best_score = max(scores)

    best_index = scores.argmax()

    return best_score, best_index


def perform_nli(evidence, answer):

    result = classifier(
        f"{evidence} [SEP] {answer}"
    )[0]

    return result["label"], result["score"]


def verify_question(question):

    # 1. Generate answer
    answer = generate_answer(question)

    # 2. Retrieve evidence
    evidence = retrieve_evidence(question)

    # 3. Calculate similarity
    similarity, best_index = calculate_similarity(
        answer,
        evidence
    )

    best_evidence = evidence[best_index]

    # 4. NLI
    nli_label, nli_score = perform_nli(
        best_evidence,
        answer
    )

    # 5. Confidence
    confidence, status = calculate_confidence(
        similarity,
        nli_label,
        nli_score
    )

    return {
        "answer": answer,
        "evidence": evidence,
        "best_evidence": best_evidence,
        "similarity": similarity,
        "nli_label": nli_label,
        "nli_score": nli_score,
        "confidence": confidence,
        "status": status
    }


if __name__ == "__main__":

    question = input("Enter your question: ")

    result = verify_question(question)

    print("\n" + "=" * 60)
    print("HALLUCINATION GUARD RESULT")
    print("=" * 60)

    print("\nGenerated Answer:")
    print(result["answer"])

    print("\nRetrieved Evidence:")
    for i, evidence in enumerate(result["evidence"], 1):
        print(f"{i}. {evidence}")

    print("\nBest Evidence:")
    print(result["best_evidence"])

    print(
        f"\nSemantic Similarity: "
        f"{result['similarity']:.4f}"
    )

    print(
        f"NLI: {result['nli_label']} "
        f"({result['nli_score']:.4f})"
    )

    print(
        f"\nConfidence Score: "
        f"{result['confidence']:.2f}%"
    )

    print(
        f"Verification Status: "
        f"{result['status']}"
    )

    print("=" * 60)