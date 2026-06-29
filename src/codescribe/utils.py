from pathlib import Path

DEFAULT_IGNORES = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "dist",
    "build",
    "codescribe.json",
}

LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".jsx": "React JSX",
    ".tsx": "React TSX",
    ".html": "HTML",
    ".css": "CSS",
    ".scss": "SCSS",
    ".java": "Java",
    ".cs": "C#",
    ".cpp": "C++",
    ".c": "C",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".rb": "Ruby",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".dart": "Dart",
    ".sql": "SQL",
    ".json": "JSON",
    ".toml": "TOML",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".md": "Markdown",
}


def should_ignore(path: Path) -> bool:
    """
    Returns True if any part of the path should be ignored.
    """
    return any(part in DEFAULT_IGNORES for part in path.parts)
