import pytest
from unittest.mock import patch

from app.processor import FileProcessor


@pytest.mark.asyncio
async def test_process_all(temp_folder):
    processor = FileProcessor(temp_folder)

    results = await processor.process_all()

    assert len(results) == 2
    assert results[0].word_count > 0


@pytest.mark.asyncio
async def testread_file_mock(temp_folder):
    processor = FileProcessor(temp_folder)

    with patch("pathlib.Path.read_text", return_value="mocked content"):
        results = await processor.process_all()

        for result in results:
            assert result.word_count == 2