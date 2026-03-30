import argparse
import asyncio
from pathlib import Path
import json

from .processor import FileProcessor


def parse_args():
    parser = argparse.ArgumentParser(
        description="Async Folder File Processor CLI"
    )
    parser.add_argument(
        "--folder",
        type=str,
        required=True,
        help="Path to folder containing files"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.json",
        help="Output JSON file"
    )
    return parser.parse_args()

async def run(folder: str, output: str):
    processor = FileProcessor(Path(folder))
    results = await processor.process_all()

    with open(output, "w") as f:
        json.dump(
            [result.model_dump() for result in results],
            f,
            indent=4,
        )


def main():
    args = parse_args()
    asyncio.run(run(args.folder, args.output))


if __name__ == "__main__":
    main()