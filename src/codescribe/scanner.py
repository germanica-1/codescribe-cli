from pathlib import Path

from .analyzers.dependency import detect_dependencies
from .analyzers.language import detect_languages
from .ignore import CodeScribeIgnore, GitIgnore
from .manifest import Manifest, ProjectInfo, Stats
from .utils import should_ignore


class ProjectScanner:
    def __init__(self, root: Path):
        self.root = root.resolve()

        self.gitignore = GitIgnore(self.root)
        self.codescribeignore = CodeScribeIgnore(self.root)

    def scan(self) -> Manifest:
        files, folders = self._scan_project()

        return Manifest(
            project=ProjectInfo(
                name=self.root.name,
                path=str(self.root),
            ),
            stats=Stats(
                files=len(files),
                folders=len(folders),
                total_items=len(files) + len(folders),
            ),
            tree=[
                str(file.relative_to(self.root))
                for file in files
            ],
            languages=detect_languages(files),
            dependencies=detect_dependencies(self.root),
        )

    def _scan_project(self) -> tuple[list[Path], list[Path]]:
        files = []
        folders = []

        for item in sorted(self.root.rglob("*")):

            if should_ignore(item):
                continue

            if self.gitignore.is_ignored(item):
                continue

            if self.codescribeignore.is_ignored(item):
                continue

            if item.is_file():
                files.append(item)

            elif item.is_dir():
                folders.append(item)

        return files, folders
