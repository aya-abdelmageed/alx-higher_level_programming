#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ans = None
    try:
        ans = fct(*args)
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(e))
    return ans
