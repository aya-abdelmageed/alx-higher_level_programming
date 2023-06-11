#!/usr/bin/python3

import sys

if __name__ != "__main__":
    exit()

strArg = "{:d} argument"
argc = len(sys.argv)
if argc == 1:
    strArg += 's.'
elif argc == 2:
    strArg += ':'
else:
    strArg += 's:'
print(strArg.format(argc))

for i in range(1, argc):
        print("{:d}: {:s}".format(i, sys.argv[i]))
