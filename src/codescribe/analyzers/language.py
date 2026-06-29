from collections import Counter
from pathlib import Path

from ..utils import LANGUAGE_MAP


def detect_languages(files: list[Path]) -> dict[str, int]:
    """
    Detect the programming languages used in a project based on file extensions.
    """
    languages = Counter()

    for file in files:
        language = LANGUAGE_MAP.get(file.suffix.lower())

        if language:
            languages[language] += 1

    return dict(languages)
