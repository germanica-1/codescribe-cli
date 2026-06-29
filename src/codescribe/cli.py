from pathlib import Path
import time

import typer

from .scanner import ProjectScanner
from .ui import (
    show_banner,
    show_dashboard,
    show_dependencies,
    show_project,
    show_tree,
    progress,
    success,
)
from .version import __version__

app = typer.Typer(
    help="Generate AI-ready project manifests."
)


@app.command()
def version():
    """Show CodeScribe version."""
    typer.echo(f"CodeScribe v{__version__}")


@app.command()
def scan(
    path: Path = typer.Argument(
        Path("."),
        help="Project directory to scan.",
    ),
):
    scanner = ProjectScanner(path)

    show_banner()

    start = time.perf_counter()

    with progress() as p:

        task = p.add_task(
            "Scanning project...",
            total=100,
        )

        manifest = scanner.scan()

        p.update(task, completed=100)

    elapsed = time.perf_counter() - start

    output = path / "codescribe.json"

    manifest.save(output)

    show_project(
        manifest.project.name,
        manifest.project.path,
    )

    show_dashboard(manifest)

    show_dependencies(
        manifest.dependencies,
    )

    show_tree(
        manifest.tree,
    )

    success(
        output.name,
        elapsed,
    )


if __name__ == "__main__":
    app()
