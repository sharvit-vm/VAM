from app.processors.txt_processor import TxtProcessor
from pathlib import Path

def test_txt_processor(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("hello world")

    processor = TxtProcessor(file)
    text = processor.extract_text()

    assert text == "hello world"
    assert processor.word_count(text) == 2