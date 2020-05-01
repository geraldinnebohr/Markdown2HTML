#!/usr/bin/python3
"""script that takes 2 arguments"""
import sys
import os.path


if __name__ == "__main__":
    lenght = len(sys.argv)
    if lenght < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    elif os.path.exists(sys.argv[1]) is False:
        print("Missing " + sys.argv[1], file=sys.stderr)
        exit(1)
    else:
        exit(0)
