
import unittest
from main import parse_document, dynamic_chunking
from retrieval import retrieve


class TestRAGProject(unittest.TestCase):

    def test_txt_parsing(self):
        from pathlib import Path
        text = parse_document(Path("documents/sample.txt"))
        self.assertTrue(len(text) > 0)

    def test_dynamic_chunking(self):
        text = " ".join(f"word{i}" for i in range(120))
        chunks = dynamic_chunking(text, chunk_size=50, overlap=10)

        self.assertEqual(len(chunks), 3)
        self.assertEqual(len(chunks[0].split()), 50)
        self.assertEqual(len(chunks[1].split()), 50)

    def test_retrieval(self):
        results = retrieve("dynamic chunking")
        self.assertTrue(len(results) > 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
