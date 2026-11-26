#!/usr/bin/env python3
"""Write the one-sentence apology entry for the make.fun bounty.

The program writes a single sentence to /output/entry.txt when that
directory is available, and falls back to a local entry.txt otherwise
so the same file can be checked during development.
"""

from pathlib import Path


APOLOGY = (
    "Sorry I told your boss you were heads-down in deep work while "
    "you were napping, then helpfully shared your screen to prove it."
)


def output_path() -> Path:
    """Return the entry path the grader reads, creating its folder."""
    target = Path("/output/entry.txt")
    try:
        target.parent.mkdir(parents=True, exist_ok=True)
        return target
    except OSError:
        return Path("entry.txt")


def main() -> None:
    """Write the apology as UTF-8 text with no extra sentence."""
    text = APOLOGY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be between 1 and 200 characters")
    path = output_path()
    path.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
