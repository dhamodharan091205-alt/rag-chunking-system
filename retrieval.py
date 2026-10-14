from pathlib import Path
import re


OUTPUT_DIR = Path("output")


def tokenize(text):
    return set(re.findall(r"\b[a-zA-Z0-9]+\b", text.lower()))


def load_chunks():
    chunks = []

    for path in OUTPUT_DIR.glob("*_chunks.txt"):
        content = path.read_text(encoding="utf-8")
        sections = re.split(r"--- Chunk \d+ ---\s*", content)

        for section in sections:
            section = section.strip()
            if section:
                chunks.append({
                    "source": path.name,
                    "text": section
                })

    return chunks


def retrieve(question, top_k=3):
    question_words = tokenize(question)

    if not question_words:
        return []

    scored_chunks = []

    for chunk in load_chunks():
        chunk_words = tokenize(chunk["text"])
        matches = question_words & chunk_words

        if matches:
            score = len(matches) / len(question_words)
            scored_chunks.append((score, chunk))

    scored_chunks.sort(key=lambda item: item[0], reverse=True)

    return scored_chunks[:top_k]


def main():
    print("RAG Document Retrieval")
    question = input("Enter your question: ").strip()

    results = retrieve(question)

    if not results:
        print("No relevant chunks found.")
        return

    print("\nRelevant results:\n")

    for rank, (score, chunk) in enumerate(results, start=1):
        print(f"Result {rank} | Score: {score:.2f}")
        print(f"Source: {chunk['source']}")
        print(chunk["text"])
        print("-" * 50)


if __name__ == "__main__":
    main()