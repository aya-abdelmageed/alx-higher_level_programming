#!/usr/bin/python3
""" Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""
    with open(filename, "r+") as f:
            lines = f.readlines()
            i = 0
            for l in lines:
                if l.find(search_string) is not -1:
                    lines.insert(i + 1, new_string)
                i += 1
            f.seek(0)
            f.write("", join(lines))
