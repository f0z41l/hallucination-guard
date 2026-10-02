from transformers import pipeline


# Load NLI model
classifier = pipeline(
    "text-classification",
    model="cross-encoder/nli-deberta-v3-base"
)


def check_nli(evidence, answer):

    result = classifier(
        f"{evidence} [SEP] {answer}"
    )[0]

    return result


if __name__ == "__main__":

    evidence = "The capital of France is Paris."

    answer = input("Enter answer: ")

    result = check_nli(evidence, answer)

    print("\nNLI Result:")
    print(result)