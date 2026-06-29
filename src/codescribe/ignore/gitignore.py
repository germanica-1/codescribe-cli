from pathlib import Path

import pathspec


class GitIgnore:
    """
    Handles .gitignore pattern matching.
    """

    def __init__(self, root: Path):
        self.root = root
        self.spec = self._load_gitignore()

    def _load_gitignore(self):
        gitignore = self.root / ".gitignore"

        if not gitignore.exists():
            return pathspec.PathSpec.from_lines(
                "gitwildmatch",
                [],
            )

        with gitignore.open(
            "r",
            encoding="utf-8",
        ) as f:
            return pathspec.PathSpec.from_lines(
                "gitwildmatch",
                f.readlines(),
            )

    def is_ignored(self, path: Path) -> bool:
        """
        Returns True if the path matches a .gitignore rule.
        """

        relative = path.relative_to(self.root)

        return self.spec.match_file(str(relative))
