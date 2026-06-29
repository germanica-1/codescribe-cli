from pathlib import Path
import tomllib


def detect_dependencies(root: Path) -> dict[str, list[str]]:
    """
    Detect project dependencies.

    Currently supports:
    - pyproject.toml
    """

    python_dependencies: list[str] = []

    pyproject = root / "pyproject.toml"

    if pyproject.exists():

        with pyproject.open("rb") as f:
            data = tomllib.load(f)

        project = data.get("project", {})

        for dependency in project.get("dependencies", []):

            name = (
                dependency.split(">=")[0]
                .split("==")[0]
                .split("<=")[0]
                .split("~=")[0]
                .strip()
            )

            python_dependencies.append(name)

    return {
        "python": sorted(set(python_dependencies)),
        "node": [],
    }
