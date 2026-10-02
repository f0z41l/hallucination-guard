def calculate_confidence(similarity, nli_label, nli_score):

    # Convert similarity from 0–1 to percentage
    similarity_score = similarity * 100

    if nli_label == "entailment":
        confidence = (
            0.5 * similarity_score +
            0.5 * (nli_score * 100)
        )

    elif nli_label == "contradiction":
        confidence = (
            0.5 * similarity_score -
            0.5 * (nli_score * 100)
        )

    else:  # neutral
        confidence = 0.5 * similarity_score

    # Keep score between 0 and 100
    confidence = max(0, min(100, confidence))

    # Verification status
    if confidence >= 85:
        status = "Verified"
    elif confidence >= 60:
        status = "Low Confidence"
    else:
        status = "Possible Hallucination"

    return confidence, status


if __name__ == "__main__":

    similarity = float(
        input("Enter similarity score (0-1): ")
    )

    nli_label = input(
        "Enter NLI label (entailment/contradiction/neutral): "
    )

    nli_score = float(
        input("Enter NLI confidence (0-1): ")
    )

    confidence, status = calculate_confidence(
        similarity,
        nli_label,
        nli_score
    )

    print(f"\nConfidence Score: {confidence:.2f}%")
    print(f"Verification Status: {status}")