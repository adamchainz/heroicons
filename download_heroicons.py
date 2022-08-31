#!/usr/bin/env python
"""
Download the latest heroicons zip file and select only the optimized icons.
"""
from __future__ import annotations

import argparse
import os
import subprocess
from io import BytesIO
from zipfile import ZIP_DEFLATED, ZipFile


def rename_file(filename: str) -> str:
    if filename.startswith("24/solid"):
        return filename.replace("24/solid", "solid")
    elif filename.startswith("24/outline"):
        return filename.replace("24/outline", "outline")
    elif filename.startswith("20/solid"):
        return filename.replace("20/solid", "mini")

    return filename


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="Git SHA")
    args = parser.parse_args(argv)
    version: str = args.version

    proc = subprocess.run(
        [
            "curl",
            "--fail",
            "--location",
            f"https://github.com/tailwindlabs/heroicons/archive/v{version}.zip",
        ],
        stdout=subprocess.PIPE,
    )
    if proc.returncode != 0:
        raise SystemExit(1)

    input_zip = ZipFile(BytesIO(proc.stdout))
    input_prefix = f"heroicons-{version}/optimized/"

    output_path = "src/heroicons/heroicons.zip"

    try:
        os.remove(output_path)
    except FileNotFoundError:
        pass
    with ZipFile(
        output_path, "w", compression=ZIP_DEFLATED, compresslevel=9
    ) as output_zip:
        for name in sorted(input_zip.namelist()):
            if name.startswith(input_prefix) and name.endswith(".svg"):
                info = input_zip.getinfo(name)
                data = input_zip.read(name)

                new_name = rename_file(name[len(input_prefix) :])

                info.filename = new_name
                output_zip.writestr(info, data)
                print(new_name)

    print("\n✅ Written!")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
