# -*- coding: utf-8 -*-

import argparse
import fnmatch
import os
import sys


def clean_files(patterns):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    clean_files_by_patterns(root_dir, patterns)
    for item in os.listdir(root_dir):
        if item.endswith("test") or item.endswith("plan") or item.endswith("lib"):
            item_path = os.path.join(root_dir, item)
            if os.path.isdir(item_path):
                clean_files_by_patterns(item_path, patterns)


def clean_files_by_patterns(dir_path, patterns):
    for temp_dir, _, file_names in os.walk(dir_path):
        for file_name in file_names:
            for pattern in patterns:
                if fnmatch.fnmatch(file_name, pattern):
                    file_path = os.path.join(temp_dir, file_name)
                    os.remove(file_path)
                    break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pattern", nargs="*", dest="patterns",
                        help="pattern to match file")
    args = parser.parse_args(sys.argv[1:])
    if not args.patterns:
        args.patterns = ["*.log"]
    clean_files(args.patterns)
