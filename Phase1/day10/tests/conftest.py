import pytest
from pathlib import Path


@pytest.fixture
def temp_folder(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"

    file1.write_text("Hello world")
    file2.write_text("Async processing test")

    return tmp_path