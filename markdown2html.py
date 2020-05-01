#!/usr/bin/python3
"""script that takes 2 arguments"""
import sys
import os.path


if __name__ == "__main__":
    lenght = len(sys.argv)
    if lenght < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        exit(1)
    elif os.path.exists(sys.argv[1]) is False:
        sys.stderr.write("Missing " + sys.argv[1])
        exit(1)
    else:
        exit(0)
