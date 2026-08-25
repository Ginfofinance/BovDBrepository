"""
Project structure mapping utility for BovDb repository.
Scans repository tree and generates visual map with file descriptions.
"""

import ast
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(".")
IGNORE_DIRS = {
    ".git", "__pycache__", ".venv", "venv", ".idea", ".vscode", "scratch"
}
TEXT_FILE_EXTENSIONS = {
    ".py", ".md", ".txt", ".yml", ".yaml", ".cff", ".toml", ".ipynb"
}


def get_python_description(file_path: Path) -> str:
    try:
        content = file_path.read_text(encoding="utf-8")
        tree = ast.parse(content)
        doc = ast.get_docstring(tree)
        if doc:
            return doc.strip().splitlines()[0]
    except Exception:
        pass
    return ""


def get_markdown_title(file_path: Path) -> str:
    try:
        content = file_path.read_text(encoding="utf-8")
        for line in content.splitlines():
            line = line.strip()
            if line.startswith("# "):
                return line.lstrip("# ").strip()
    except Exception:
        pass
    return ""


def get_file_description(file_path: Path) -> str:
    suffix = file_path.suffix.lower()
    if suffix == ".py":
        desc = get_python_description(file_path)
        if desc:
            return desc
    elif suffix == ".md":
        title = get_markdown_title(file_path)
        if title:
            return title
    elif file_path.name == "CITATION.cff":
        return "Academic citation metadata (Citation File Format)"
    elif file_path.name == "LICENSE.md":
        return "Creative Commons CC BY-NC 4.0 International License"
    elif file_path.name == "requirements.txt":
        return "Python project dependencies"
    elif file_path.name == "pyproject.toml":
        return "Python package build configuration and metadata"
    elif file_path.name == "link_database.txt":
        return "Official database download links and mirrors"
    elif file_path.name.endswith(".zip"):
        return "Historical dataset archive"
    elif file_path.name.endswith(".pdf"):
        return "Database extraction and user guidelines (PDF)"
    elif file_path.name == ".gitignore":
        return "Git ignore rules for binaries, database files, and caches"
    elif file_path.name == ".env.example":
        return "Example environment configuration template"
    return ""


def build_tree(directory: Path, prefix: str = "") -> list:
    lines = []
    items = sorted(
        [p for p in directory.iterdir() if p.name not in IGNORE_DIRS],
        key=lambda x: (not x.is_dir(), x.name.lower())
    )

    for i, item in enumerate(items):
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        child_prefix = "    " if is_last else "│   "

        if item.is_dir():
            lines.append(f"{prefix}{connector}{item.name}/")
            lines.extend(build_tree(item, prefix + child_prefix))
        else:
            desc = get_file_description(item)
            desc_str = f" # {desc}" if desc else ""
            lines.append(f"{prefix}{connector}{item.name}{desc_str}")

    return lines


def main():
    print("Generating BovDB repository layout tree...")
    lines = [f"{ROOT_DIR.resolve().name}/"] + build_tree(ROOT_DIR)
    tree_text = "\n".join(lines)
    print("\n" + tree_text)


if __name__ == "__main__":
    main()
