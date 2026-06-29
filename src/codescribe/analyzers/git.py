from pathlib import Path
import subprocess

from ..manifest import GitInfo


def run_git(root: Path, *args) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            capture_output=True,
            text=True,
            check=True,
        )

        return result.stdout.strip()

    except Exception:
        return None


def detect_git(root: Path) -> GitInfo:

    inside = run_git(
        root,
        "rev-parse",
        "--is-inside-work-tree",
    )

    if inside != "true":
        return GitInfo()

    return GitInfo(
        repository=True,

        branch=run_git(
            root,
            "branch",
            "--show-current",
        ),

        remote_name=run_git(
            root,
            "remote",
        ),

        remote_url=run_git(
            root,
            "config",
            "--get",
            "remote.origin.url",
        ),

        latest_commit=run_git(
            root,
            "rev-parse",
            "--short",
            "HEAD",
        ),

        latest_message=run_git(
            root,
            "log",
            "-1",
            "--pretty=%s",
        ),

        dirty=bool(
            run_git(
                root,
                "status",
                "--porcelain",
            )
        ),
    )
