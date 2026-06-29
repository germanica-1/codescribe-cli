from pathlib import Path

import typer
from rich import print

from .scanner import ProjectScanner


app = typer.Typer(
    help="Generate AI-ready project manifests."
)


@app.command()
def version():
    """
    Show the current CodeScribe version.
    """
    print(f"[bold cyan]CodeScribe[/bold cyan] v{__version__}")


@app.command()
def scan(
    directory: Path = typer.Argument(
        Path("."),
        help="Project directory to scan.",
    ),
):
    """
    Scan a project directory.
    """

    if not directory.exists():
        print("[red]Directory does not exist.[/red]")
        raise typer.Exit(1)

    print("[cyan]Scanning project...[/cyan]")

    scanner = ProjectScanner(directory)

    manifest = scanner.scan()

    output = directory / "codescribe.json"

    manifest.save(output)

    print(f"[green]✓ Manifest written to {output}[/green]")

if __name__ == "__main__":
    app()
