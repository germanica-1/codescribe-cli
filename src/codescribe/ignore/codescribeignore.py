from pathlib import Path

import pathspec


class CodeScribeIgnore:
    """
    Handles .codescribeignore pattern matching.
    """

    def __init__(self, root: Path):
        self.root = root
        self.spec = self._load_codescribeignore()

    def _load_codescribeignore(self):
        ignore_file = self.root / ".codescribeignore"

        if not ignore_file.exists():
            return pathspec.PathSpec.from_lines(
                "gitwildmatch",
                [],
            )

        with ignore_file.open(
            "r",
            encoding="utf-8",
        ) as f:
            return pathspec.PathSpec.from_lines(
                "gitwildmatch",
                f.readlines(),
            )

    def is_ignored(self, path: Path) -> bool:
        relative = path.relative_to(self.root)
        return self.spec.match_file(str(relative))
