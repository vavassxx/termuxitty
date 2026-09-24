#!/usr/bin/env python3
"""Rewrite the Termux bootstrap's hard-coded package path for Termuxitty.

The Android application id is intentionally the same byte length as the upstream
`com.termux` id, so the replacement is safe inside ELF/string data without
requiring a rebuild of every bootstrap binary.
"""
from __future__ import annotations

import argparse
import io
import zipfile
from pathlib import Path

OLD = b"com.termux"
NEW = b"com.ttymux"
assert len(OLD) == len(NEW)


def patch(path: Path) -> None:
    source = zipfile.ZipFile(path, "r")
    output = io.BytesIO()
    replacements = 0
    with source, zipfile.ZipFile(output, "w") as dest:
        for info in source.infolist():
            data = source.read(info.filename)
            count = data.count(OLD)
            if count:
                data = data.replace(OLD, NEW)
                replacements += count
            dest.writestr(info, data)
    path.write_bytes(output.getvalue())
    if replacements == 0:
        raise SystemExit(f"No {OLD!r} references found in {path}")
    print(f"Patched {path}: {replacements} package references")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("zip", type=Path)
    args = parser.parse_args()
    patch(args.zip)
