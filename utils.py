from pathlib import Path
from typing import List


def extract_text(input_text: str):
    return [ligne.strip() for ligne in input_text.splitlines() if ligne.strip()]

def import_text(text_path: Path) -> List[str]:
    with open(text_path, 'r') as f:
        return f.read().splitlines()