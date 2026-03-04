import asyncio
from pathlib import Path
from typing import List

from .models import FileResult
from .logger import setup_logger

logger = setup_logger()


class FileProcessor:
    def __init__(self, folder: Path):
        self.folder = folder

    async def process_file(self, path: Path) -> FileResult | None:
        logger.info(f"Processing {path.name}")

        try:
            content = await self.read_file(path)
            result = FileResult.from_path(path, content)
            logger.info(f"Finished {path.name}")
            return result

        except Exception as e:
            logger.error(f"Failed to process {path.name}: {e}")
            return None

    async def read_file(self, path: Path) -> str:
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, path.read_text)

    async def process_all(self) -> List[FileResult]:
        tasks = []

        for file in self.folder.iterdir():
            # Only process .txt files
            if file.is_file() and file.suffix == ".txt":
                tasks.append(self.process_file(file))

        results = await asyncio.gather(*tasks)

        # Remove failed results (None)
        return [result for result in results if result is not None]