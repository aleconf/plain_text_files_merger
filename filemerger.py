#!/usr/bin/env python

import chardet
import io
import os
# from pathlib import Path
import shutil


def is_plain_text_file(path):
    """Check if the input is a plain text file.

    Tested with https://github.com/stain/encoding-test-files
    and https://www.kermitproject.org/utf8.html
    """

    with open(path, "rb") as file:
        data = file.read()
        result = chardet.detect(data)
        if (
            result["encoding"] is None
            or result["encoding"] == "UTF-16"
            or result["encoding"] == "UTF-32"
        ):
            return False
        else:
            return True


def merger(input_dir, separator, output_dir, output_file):
    """Merging all plain text files.

    A line containing a given string is used as a separator.
    """
    file_list = [
        os.path.join(input_dir, f)
        for f in os.listdir(input_dir)
        if os.path.isfile(os.path.join(input_dir, f))
        and is_plain_text_file(os.path.join(input_dir, f))
        and f[0] != "."
    ]
    #    file_list = list()
    #    for current_path, _, files in os.walk(input_dir):
    #        if Path(current_path) != Path(input_dir):
    #            continue
    #        for filename in files:
    #            full_file = os.path.join(input_dir, filename)
    #            if is_plain_text_file(full_file) and filename[0] != ".":
    #                file_list.append(full_file)

    with open(os.path.join(output_dir, output_file), "wb") as merged_file:
        for i, f in enumerate(file_list):
            with open(f, "rb") as elem:
                shutil.copyfileobj(elem, merged_file)
            if i < len(file_list) - 1:
                # elem = io.BytesIO(b"\n\n")
                encoded_separator = ("\n" + separator + "\n").encode()
                elem = io.BytesIO(encoded_separator)
                shutil.copyfileobj(elem, merged_file)


def main():
    flag = True
    while flag:
        text_dir = input(
            "\nPlease, insert the full path of the directory containing "
            + "the plain text files to be merged. \n"
        )
        if os.path.isdir(text_dir):
            flag = False
        else:
            print("    Directory is invalid or non-existent.")

    separating = input(
        "\nPlease, insert the string to write in the line separating the "
        + "different files (press Enter for a blank line). \n"
    )

    flag = True
    while flag:
        saving_dir = input(
            "\nPlease, insert the full path of the directory where the "
            + "result should be saved. \n"
        )
        if os.path.isdir(saving_dir):
            flag = False
        else:
            print("    Directory is invalid or non-existent.")

    flag = True
    while flag:
        saving_file = input(
            "\nPlease, insert the filename (e.g. result.xyz) where the "
            + "result should be saved. \n"
        )
        check_file = os.path.join(saving_dir, saving_file)
        if os.path.isfile(check_file):
            print("    The file already exists: please choose another name.")
        else:
            flag = False

    merger(text_dir, separating, saving_dir, saving_file)


if __name__ == "__main__":
    main()
