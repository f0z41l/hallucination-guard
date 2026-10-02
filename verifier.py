def calculate_confidence(similarity, nli_label, nli_score):

    similarity_score = similarity * 100

    # Evidence supports the answer
    if nli_label == "entailment":

        confidence = (
            0.5 * similarity_score +
            0.5 * (nli_score * 100)
        )

        if confidence >= 85:
            status = "Verified"
        else:
            status = "Low Confidence"

    # Evidence contradicts the answer
    elif nli_label == "contradiction":

        confidence = (
            0.5 * similarity_score -
            0.5 * (nli_score * 100)
        )

        confidence = max(0, confidence)

        status = "Possible Hallucination"

    # Evidence is insufficient to verify the answer
    else:  # neutral

        confidence = 0.5 * similarity_score

        status = "Low Confidence"

    confidence = max(0, min(100, confidence))

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