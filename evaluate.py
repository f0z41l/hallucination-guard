import csv

from pipeline import calculate_similarity, perform_nli
from verifier import calculate_confidence
from test_dataset import test_cases


# Load evidence from knowledge base
with open(
    "data/knowledge_base.txt",
    "r",
    encoding="utf-8"
) as file:

    evidence_data = [
        line.strip()
        for line in file
        if line.strip()
    ]


def find_best_evidence(answer):

    similarity, index = calculate_similarity(
        answer,
        evidence_data
    )

    return similarity, evidence_data[index]


def run_evaluation():

    results = []

    for i, test in enumerate(test_cases, 1):

        similarity, evidence = find_best_evidence(
            test["answer"]
        )

        nli_label, nli_score = perform_nli(
            evidence,
            test["answer"]
        )

        confidence, status = calculate_confidence(
            similarity,
            nli_label,
            nli_score
        )

        correct = status == test["expected"]

        result = {
            "test_id": i,
            "question": test["question"],
            "answer": test["answer"],
            "evidence": evidence,
            "similarity": round(similarity, 4),
            "nli_label": nli_label,
            "nli_score": round(nli_score, 4),
            "confidence": round(confidence, 2),
            "predicted_status": status,
            "expected_status": test["expected"],
            "correct": correct
        }

        results.append(result)

        print(
            f"Test {i:02d}/{len(test_cases)} | "
            f"{status} | "
            f"{'Correct' if correct else 'Incorrect'}"
        )


    # Save results
    with open(
        "evaluation_results.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        fieldnames = [
            "test_id",
            "question",
            "answer",
            "evidence",
            "similarity",
            "nli_label",
            "nli_score",
            "confidence",
            "predicted_status",
            "expected_status",
            "correct"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(results)


    # Basic accuracy
    correct_count = sum(
        result["correct"]
        for result in results
    )

    accuracy = (
        correct_count / len(results)
    ) * 100


    print("\n" + "=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)

    print(f"Total Tests : {len(results)}")
    print(f"Correct     : {correct_count}")
    print(f"Incorrect   : {len(results) - correct_count}")
    print(f"Accuracy    : {accuracy:.2f}%")

    print("\nResults saved to:")
    print("evaluation_results.csv")


if __name__ == "__main__":
    run_evaluation()

    