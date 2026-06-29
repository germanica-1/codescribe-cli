from ..manifest import Frameworks

FRAMEWORK_MAP = {
    # ==========================
    # Python
    # ==========================
    "fastapi": ("backend", "FastAPI"),
    "django": ("backend", "Django"),
    "flask": ("backend", "Flask"),

    "typer": ("cli", "Typer"),
    "click": ("cli", "Click"),

    "sqlalchemy": ("orm", "SQLAlchemy"),
    "peewee": ("orm", "Peewee"),
    "tortoise-orm": ("orm", "Tortoise ORM"),

    "pytest": ("testing", "Pytest"),
    "unittest": ("testing", "unittest"),

    # ==========================
    # Node
    # ==========================
    "express": ("backend", "Express"),
    "nestjs": ("backend", "NestJS"),

    "react": ("frontend", "React"),
    "next": ("frontend", "Next.js"),
    "vue": ("frontend", "Vue"),
    "nuxt": ("frontend", "Nuxt"),
    "angular": ("frontend", "Angular"),

    "tailwindcss": ("styling", "Tailwind CSS"),

    "vite": ("build", "Vite"),
    "webpack": ("build", "Webpack"),

    "jest": ("testing", "Jest"),
}


def detect_frameworks(dependencies: dict) -> Frameworks:
    frameworks = Frameworks()

    for ecosystem in dependencies.values():
        for package in ecosystem:

            if package not in FRAMEWORK_MAP:
                continue

            category, framework = FRAMEWORK_MAP[package]

            getattr(frameworks, category).append(framework)

    return frameworks
