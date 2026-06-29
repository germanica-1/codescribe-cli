from datetime import datetime, timezone
from pathlib import Path
import json

from pydantic import BaseModel, Field


class ProjectInfo(BaseModel):
    name: str
    path: str


class Stats(BaseModel):
    files: int
    folders: int
    total_items: int


class Frameworks(BaseModel):
    backend: list[str] = Field(default_factory=list)
    frontend: list[str] = Field(default_factory=list)
    cli: list[str] = Field(default_factory=list)
    orm: list[str] = Field(default_factory=list)
    testing: list[str] = Field(default_factory=list)
    styling: list[str] = Field(default_factory=list)
    build: list[str] = Field(default_factory=list)


class GitInfo(BaseModel):
    repository: bool = False

    branch: str | None = None

    remote_name: str | None = None

    remote_url: str | None = None

    latest_commit: str | None = None

    latest_message: str | None = None

    dirty: bool = False


class Manifest(BaseModel):
    manifest_version: str = "1.0"

    generated_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    project: ProjectInfo

    stats: Stats

    tree: list[str]

    languages: dict[str, int]

    dependencies: dict[str, list[str]]

    frameworks: Frameworks

    git: GitInfo

    def save(self, output: Path):
        output.write_text(
            json.dumps(
                self.model_dump(),
                indent=4,
            ),
            encoding="utf-8",
        )
