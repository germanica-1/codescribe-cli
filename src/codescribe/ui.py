from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns
from rich.tree import Tree
from rich.progress import (
    Progress,
    SpinnerColumn,
    BarColumn,
    TextColumn,
    TimeElapsedColumn,
)

console = Console()


def show_banner():
    console.print(
        Panel.fit(
            "[bold cyan]CodeScribe[/bold cyan]\n"
            "[dim]Project Manifest Generator[/dim]",
            border_style="cyan",
        )
    )


def show_project(name: str, path: str):
    table = Table(show_header=False, box=None)

    table.add_column(style="cyan", width=10)
    table.add_column()

    table.add_row("Name", name)
    table.add_row("Path", path)

    console.print(Panel(table, title="📂 Project"))


def show_dashboard(manifest):
    stats = manifest.stats

    summary = Table(title="Summary")

    summary.add_column("Metric")
    summary.add_column("Value", justify="right")

    summary.add_row("Files", str(stats.files))
    summary.add_row("Folders", str(stats.folders))
    summary.add_row("Languages", str(len(manifest.languages)))

    dep_count = (
        len(manifest.dependencies["python"])
        + len(manifest.dependencies["node"])
    )

    summary.add_row("Dependencies", str(dep_count))

    languages = Table(title="Languages")

    languages.add_column("Language")
    languages.add_column("Files", justify="right")

    for lang, count in sorted(
        manifest.languages.items(),
        key=lambda x: x[1],
        reverse=True,
    ):
        languages.add_row(lang, str(count))

    console.print(Columns([summary, languages]))


def show_dependencies(dependencies):
    table = Table(title="📦 Dependencies")

    table.add_column("Language")
    table.add_column("Packages")

    for lang, pkgs in dependencies.items():
        if not pkgs:
            continue

        table.add_row(
            lang.capitalize(),
            "\n".join(f"• {pkg}" for pkg in pkgs),
        )

    console.print(table)


def show_tree(tree: list[str], limit: int = 12):
    root = Tree("📁 Project")

    shown = tree[:limit]

    for item in shown:
        root.add(item)

    remaining = len(tree) - limit

    if remaining > 0:
        root.add(f"... and {remaining} more")

    console.print(root)


def success(output, elapsed):
    console.print()

    console.print(
        Panel.fit(
            f"[bold green]✓ Scan completed[/bold green]\n\n"
            f"Output : [cyan]{output}[/cyan]\n"
            f"Time   : [yellow]{elapsed:.3f}s[/yellow]",
            border_style="green",
        )
    )


def progress():
    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TimeElapsedColumn(),
        transient=True,
    )
