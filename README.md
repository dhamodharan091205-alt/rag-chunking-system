# RAG Dynamic Parsing and Dynamic Chunking

## Project Overview
This project implements document parsing, dynamic text chunking, keyword-based retrieval, and a basic retrieval-augmented question-answering prototype.

## Features
- Extract text from TXT, PDF, and DOCX documents.
- Clean and normalize extracted text.
- Split documents into chunks using configurable chunk size and overlap.
- Save generated chunks as text files.
- Retrieve relevant chunks using keyword matching.
- Display retrieved context for a user question.
- Run automated tests using Python unittest.

## Technologies Used
- Python
- pypdf
- python-docx
- Regular Expressions
- Python unittest

## Project Structure
```text
project/
├── main.py
├── retrieval.py
├── rag_answer.py
├── test_project.py
├── documents/
│   ├── sample.txt
│   ├── long_sample.txt
│   ├── test_document.docx
│   └── rag_test.pdf
└── output/
    └── Generated chunk files
```

## Installation
Install the required libraries:

```bash
python -m pip install pypdf python-docx
```

## Run the Project
Process documents and generate chunks:

```bash
python main.py
```

Retrieve relevant chunks:

```bash
python retrieval.py
```

Run the question-answering prototype:

```bash
python rag_answer.py
```

Run automated tests:

```bash
python -m unittest test_project.py
```

## Current Limitations
- Retrieval uses keyword matching rather than semantic embeddings.
- The question-answering module displays retrieved context; it does not yet generate answers using an LLM.
- Scanned PDFs may require OCR.
- Chunking currently uses word counts rather than document structure.

## Future Enhancements
- Add semantic embeddings and vector search.
- Integrate an LLM for context-grounded answer generation.
- Improve structure-aware parsing and chunking.
- Add more automated tests for PDF and DOCX documents.

## Testing
Three automated tests currently pass for TXT parsing, dynamic chunking, and retrieval.