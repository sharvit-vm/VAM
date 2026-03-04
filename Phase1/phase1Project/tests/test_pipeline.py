import pytest
from unittest.mock import AsyncMock, patch
from app.pipeline import DocumentPipeline
from pathlib import Path
@pytest.mark.asyncio
@patch("app.pipeline.LanguageService.detect_language", new_callable=AsyncMock)
async def test_pipeline(mock_detect, tmp_path):
    mock_detect.return_value = "English"
    file = tmp_path / "sample.txt"
    file.write_text("hello world")

    pipeline = DocumentPipeline()
    results = await pipeline.run([file])

    assert results[0].language == "English"
    assert results[0].word_count == 2