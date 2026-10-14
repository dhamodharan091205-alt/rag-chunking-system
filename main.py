import re
from pathlib import Path
from pypdf import PdfReader
from docx import Document


INPUT_DIR = Path("documents")
OUTPUT_DIR = Path("output")
CHUNK_SIZE = 150
CHUNK_OVERLAP = 30


def parse_txt(path):
    return path.read_text(encoding="utf-8")


def parse_pdf(path):
    reader = PdfReader(str(path))
    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append(f"[Page {page_number}]\n{text}")

    return "\n\n".join(pages)


def parse_docx(path):
    doc = Document(str(path))
    parts = []

    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()
        if text:
            parts.append(text)

    for table in doc.tables:
        for row in table.rows:
            parts.append(" | ".join(cell.text.strip() for cell in row.cells))

    return "\n".join(parts)


def parse_document(path):
    suffix = path.suffix.lower()

    if suffix == ".txt":
        text = parse_txt(path)
    elif suffix == ".pdf":
        text = parse_pdf(path)
    elif suffix == ".docx":
        text = parse_docx(path)
    else:
        raise ValueError(f"Unsupported file type: {suffix}")

    text = text.replace("\r\n", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def dynamic_chunking(text, chunk_size=50,
                     overlap=10):
    if chunk_size <= 0 or overlap < 0 or overlap >= chunk_size:
        raise ValueError("Invalid chunk size or overlap")

    words = text.split()
    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))
        chunks.append(" ".join(words[start:end]))

        if end == len(words):
            break

        start = end - overlap

    return chunks


def main():
    INPUT_DIR.mkdir(exist_ok=True)
    OUTPUT_DIR.mkdir(exist_ok=True)

    files = [
        path for path in INPUT_DIR.iterdir()
        
    if path.is_file()
       and not path.name.startswith("~$")
       and path.suffix.lower() in {".txt", ".pdf", ".docx"}
    ]

    if not files:
        print("No documents found.")
        print("Add a .txt, .pdf, or .docx file to the documents folder.")
        return

    for path in files:
        try:
            text = parse_document(path)

            if not text:
                print(f"Skipped empty document: {path.name}")
                continue

            chunks = dynamic_chunking(text)
            output_path = OUTPUT_DIR / f"{path.stem}_chunks.txt"

            with output_path.open("w", encoding="utf-8") as file:
                for index, chunk in enumerate(chunks, start=1):
                    file.write(f"--- Chunk {index} ---\n")
                    file.write(chunk + "\n\n")

            print(f"File: {path.name}")
            print(f"Chunks created: {len(chunks)}")
            print(f"Output: {output_path}")

        except Exception as error:
            print(f"Error processing {path.name}: {error}")


if __name__ == "__main__":
    main()