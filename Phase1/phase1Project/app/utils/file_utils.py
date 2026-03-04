from pathlib import Path

def get_files_from_folder(folder: str):
    path = Path(folder)
    if not path.exists():
        raise FileNotFoundError("Folder does not exist")
    return [file for file in path.iterdir() if file.is_file()]