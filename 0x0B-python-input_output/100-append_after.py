#!/usr/bin/python3
""" Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""
    with open(filename, "r+") as f:
            lines = f.readlines()
            new = []
            for l in range(len(lines)):
                new.append(lines[l])
                if search_string in lines[l]:
                    new.append(new_string)
                
            f.seek(0)
            f.write("", join(new))
