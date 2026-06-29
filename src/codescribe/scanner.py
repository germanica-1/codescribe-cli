from collections import Counter
from pathlib import Path

from .manifest import Manifest, ProjectInfo, Stats
from .utils import LANGUAGE_MAP, should_ignore


class ProjectScanner:
    def __init__(self, root: Path):
        self.root = root.resolve()

    def scan(self) -> Manifest:
        files = self._collect_files()
        folders = self._count_folders()

        return Manifest(
            project=ProjectInfo(
                name=self.root.name,
                path=str(self.root),
            ),
            stats=Stats(
                files=len(files),
                folders=folders,
                total_items=len(files) + folders,
            ),
            tree=[
                str(file.relative_to(self.root))
                for file in files
            ],
            languages=self._detect_languages(files),
        )

    def _collect_files(self) -> list[Path]:
        files = []

        for item in sorted(self.root.rglob("*")):
            if should_ignore(item):
                continue

            if item.is_file():
                files.append(item)

        return files

    def _count_folders(self) -> int:
        count = 0

        for item in self.root.rglob("*"):
            if should_ignore(item):
                continue

            if item.is_dir():
                count += 1

        return count

    def _detect_languages(
        self,
        files: list[Path],
    ) -> dict[str, int]:
        languages = Counter()

        for file in files:
            language = LANGUAGE_MAP.get(file.suffix.lower())

            if language:
                languages[language] += 1

        return dict(languages)
