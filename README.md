# CodeScribe CLI

> Generate project manifests from any codebase.

CodeScribe CLI is a Python command-line tool that analyzes a software project and generates a structured JSON manifest describing the project.

Instead of providing an AI model with an entire source code repository, CodeScribe extracts important project metadata such as:

* Project information
* Directory structure
* Programming languages
* Dependencies
* Frameworks
* Git repository metadata

The generated `codescribe.json` can then be used as context for AI-powered documentation, project understanding, or future tooling.

---

# Features

* Project directory scanning
* File tree generation
* Project statistics
* Programming language detection
* Python dependency detection (`pyproject.toml`)
* Node dependency detection (`package.json`)
* Framework detection
* Git repository analysis
* `.gitignore` support
* `.codescribeignore` support
* Rich terminal interface
* JSON manifest generation

---

# Requirements

* Python **3.12** or newer
* Git (optional, but recommended)

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/germanica-1/codescribe-cli.git
```

## 2. Enter the project

```bash
cd codescribe-cli
```

## 3. Create a virtual environment

```bash
uv venv
```

## 4. Activate the virtual environment

### Linux / macOS

```bash
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

## 5. Install the project as a CLI tool

```bash
uv tool install -e .
```

The `-e` flag installs CodeScribe in **editable mode**, allowing you to modify the source code without reinstalling the tool after every change.

## 6. Verify the installation

```bash
codescribe version
```

Example output:

```text
CodeScribe v0.1.0
```

If you see the version printed, the installation was successful.

---

# Usage

## Scan the current project

Navigate to any project directory and run:

```bash
codescribe scan .
```

Example:

```bash
cd ~/Desktop/projects/MyProject
codescribe scan .
```

A file named:

```text
codescribe.json
```

will be created inside the scanned project.

---

## Scan another project

You can also scan projects without changing directories.

Example:

```bash
codescribe scan ~/Desktop/projects/Photobooth
```

or

```bash
codescribe scan ~/Desktop/projects/E-Quakes
```

---

# Output

After scanning, CodeScribe generates a file named:

```text
codescribe.json
```

The manifest currently contains:

* Project information
* Project statistics
* File tree
* Programming languages
* Dependencies
* Framework detection
* Git repository metadata

---

# Ignoring Files

CodeScribe automatically respects your project's `.gitignore`.

If a file or folder is ignored by Git, it will also be ignored by CodeScribe.

---

# `.codescribeignore`

Sometimes you may want to exclude files that are **not** in `.gitignore` but should also be omitted from the generated manifest.

For this purpose, create a file named:

```text
.codescribeignore
```

inside the root of the project you are scanning.

Example:

```text
README.md
docs/
*.log
*.tmp
notes.txt
```

When you run:

```bash
codescribe scan .
```

those files and folders will not appear in the generated `codescribe.json`.

---

## Example

Project:

```text
MyProject/
│
├── README.md
├── docs/
├── src/
├── notes.txt
└── .codescribeignore
```

Contents of `.codescribeignore`:

```text
README.md
docs/
notes.txt
```

Generated manifest tree:

```text
src/
```

The ignored files are excluded from the scan.

---

# Example Workflow

```bash
cd ~/Desktop/projects/MyProject

codescribe scan .
```

Result:

```text
MyProject/
│
├── codescribe.json
├── src/
├── pyproject.toml
└── package.json
```

You can now use `codescribe.json` as structured context for AI tools or inspect it manually.

---

# Development

After making changes to the source code, simply run:

```bash
codescribe scan .
```

Because CodeScribe was installed using:

```bash
uv tool install -e .
```

there is **no need to reinstall** after every code change.

---

# Current Capabilities

* Project scanning
* Language detection
* Dependency detection
* Framework detection
* Git analysis
* Rich CLI dashboard
* Manifest generation
* Custom ignore rules

---

# License
This project was built primarily as a personal learning and portfolio project. Contributions, experimentation, and feedback are welcome.
This project was built primarily as a personal learning and portfolio project. Contributions, experimentation, and feedback are welcome.


