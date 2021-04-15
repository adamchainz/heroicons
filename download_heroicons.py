#!/usr/bin/env python
"""
Download the latest heroicons zip file and select only the optimized icons.
"""
import argparse
import os
import sys
from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED

import requests


def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("version", help="e.g. 1.0.1")
    args = parser.parse_args(args)
    version = args.version

    zip_url = (
        f"https://github.com/tailwindlabs/heroicons/archive/refs/tags/v{version}.zip"
    )
    response = requests.get(zip_url)
    if response.status_code != 200:
        print(f"Got status code {response.status_code} for {zip_url}", file=sys.stderr)
        return 1

    input_zip = ZipFile(BytesIO(response.content))
    input_prefix = f"heroicons-{version}/optimized/"

    output_path = "src/heroicons/heroicons.zip"

    try:
        os.remove(output_path)
    except FileNotFoundError:
        pass
    with ZipFile(
        output_path, "w", compression=ZIP_DEFLATED, compresslevel=9
    ) as output_zip:
        for name in input_zip.namelist():
            if name.startswith(input_prefix) and name.endswith(".svg"):
                data = input_zip.read(name)
                new_name = name[len(input_prefix) :]
                output_zip.writestr(new_name, data)
                print(new_name)

    print("\n✅ Written!")

    return 0


if __name__ == "__main__":
    exit(main())
