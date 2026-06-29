from datetime import UTC, datetime
from pathlib import Path

from pydantic import BaseModel, Field


class ProjectInfo(BaseModel):
    name: str
    path: str


class Stats(BaseModel):
    files: int
    folders: int
    total_items: int


class Manifest(BaseModel):
    manifest_version: str = "1.0"

    generated_at: str = Field(
        default_factory=lambda: datetime.now(UTC).isoformat()
    )

    project: ProjectInfo

    stats: Stats

    tree: list[str]

    languages: dict[str, int]

    def save(self, output: Path) -> None:
        output.write_text(
            self.model_dump_json(indent=4),
            encoding="utf-8",
        )
