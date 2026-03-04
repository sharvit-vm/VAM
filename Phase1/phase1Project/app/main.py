import argparse
import asyncio
import json
import os
from dotenv import load_dotenv
from app.pipeline import DocumentPipeline
from app.utils.file_utils import get_files_from_folder
from app.utils.logger import logger

load_dotenv()

def main():
    logger.info("Application started")
    parser = argparse.ArgumentParser(description="Smart Document Processor")
    parser.add_argument("folder", help="Folder containing documents")
    args = parser.parse_args()

    # Just to Validate environment variables
    if not os.getenv("API_URL") or not os.getenv("API_KEY"):
        logger.error("Missing API_URL or API_KEY in environment")
        raise RuntimeError("Environment variables not configured properly")
    logger.info(f"Scanning folder: {args.folder}")
    files = get_files_from_folder(args.folder)
    if not files:
        logger.warning("No files found in the folder")
        return
    logger.info(f"Found {len(files)} file(s)")
    pipeline = DocumentPipeline()
    try:
        results = asyncio.run(pipeline.run(files))
    except Exception as e:
        logger.error(f"Pipeline execution failed: {e}")
        raise
    output = [result.model_dump(mode="json") for result in results]
    with open("output.json", "w") as f:
        json.dump(output, f, indent=4)
    logger.info("Output written to output.json")
    logger.info("Processing completed successfully")

if __name__ == "__main__":
    main()