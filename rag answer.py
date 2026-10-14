from retrieval import retrieve


def generate_answer(question):
    results = retrieve(question, top_k=3)

    if not results:
        return "No relevant information found in the documents."

    context = "\n\n".join(
        chunk["text"] for _, chunk in results
    )

    return (
        "Answer based on the retrieved document context:\n\n"
        f"{context}\n\n"
        "Note: This is retrieved context, not an AI-generated summary."
    )


def main():
    print("RAG Question Answering")
    question = input("Ask a question: ").strip()

    if not question:
        print("Please enter a question.")
        return

    answer = generate_answer(question)
    print("\n" + answer)


if __name__ == "__main__":
    main()