#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()

strArg = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    strArg += 's.'
elif argc == 1:
    strArg += ':'
else:
    strArg += 's:'
print(strArg.format(argc))

i = 0
for arg in sys.argv:
    if i != 0:
        print(f"{i:d}: {arg:s}")

    i += 1
