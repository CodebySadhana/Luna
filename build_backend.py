from __future__ import annotations

import base64
import csv
import hashlib
import os
from pathlib import Path
from typing import Iterable
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

NAME = "luna"
VERSION = "0.1.0"
WHEEL_NAME = f"{NAME}-{VERSION}-py3-none-any.whl"
DIST_INFO = f"{NAME}-{VERSION}.dist-info"
PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"


def _metadata() -> str:
    return "\n".join([
        "Metadata-Version: 2.1",
        f"Name: {NAME}",
        f"Version: {VERSION}",
        "Summary: Luna: the editorial intelligence layer for content strategy",
        "",
    ])


def _wheel() -> str:
    return "\n".join([
        "Wheel-Version: 1.0",
        "Generator: luna.build_backend",
        "Root-Is-Purelib: true",
        "Tag: py3-none-any",
        "",
    ])


def _entry_points() -> str:
    return "\n".join([
        "[console_scripts]",
        "luna = luna.cli:main",
        "",
    ])


def _record_rows(files: Iterable[str]) -> str:
    rows: list[list[str]] = []
    for file_name in files:
        rows.append([file_name, "", ""])
    output: list[str] = []
    from io import StringIO

    buf = StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerows(rows)
    output.append(buf.getvalue().rstrip("\n"))
    return "\n".join(output) + "\n"


def _write_wheel(wheel_directory: str, editable: bool) -> str:
    wheel_dir = Path(wheel_directory)
    wheel_dir.mkdir(parents=True, exist_ok=True)
    wheel_path = wheel_dir / WHEEL_NAME
    pth_target = str(SRC_DIR)
    dist_files = [
        f"{NAME}.pth",
        f"{DIST_INFO}/METADATA",
        f"{DIST_INFO}/WHEEL",
        f"{DIST_INFO}/entry_points.txt",
        f"{DIST_INFO}/RECORD",
    ]
    with ZipFile(wheel_path, "w", compression=ZIP_DEFLATED) as zf:
        zf.writestr(f"{NAME}.pth", pth_target + "\n")
        zf.writestr(f"{DIST_INFO}/METADATA", _metadata())
        zf.writestr(f"{DIST_INFO}/WHEEL", _wheel())
        zf.writestr(f"{DIST_INFO}/entry_points.txt", _entry_points())
        zf.writestr(f"{DIST_INFO}/RECORD", _record_rows(dist_files))
    return wheel_path.name


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    return _write_wheel(wheel_directory, editable=False)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    return _write_wheel(wheel_directory, editable=True)


def get_requires_for_build_wheel(config_settings=None):
    return []


def get_requires_for_build_editable(config_settings=None):
    return []


def prepare_metadata_for_build_wheel(metadata_directory, config_settings=None):
    dist = Path(metadata_directory) / DIST_INFO
    dist.mkdir(parents=True, exist_ok=True)
    (dist / "METADATA").write_text(_metadata(), encoding="utf-8")
    (dist / "WHEEL").write_text(_wheel(), encoding="utf-8")
    (dist / "entry_points.txt").write_text(_entry_points(), encoding="utf-8")
    (dist / "RECORD").write_text("", encoding="utf-8")
    return DIST_INFO


def prepare_metadata_for_build_editable(metadata_directory, config_settings=None):
    return prepare_metadata_for_build_wheel(metadata_directory, config_settings)
