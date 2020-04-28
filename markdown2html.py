#!/usr/bin/python3
"""frfrgt"""
if __name__ == "__main__":
    from sys import argv, stderr
    import os.path
    lenght = len(argv)
    if lenght < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=stderr)
        exit(1)
    elif os.path.exists('argv[1]') is False:
        print("Missing " + argv[1], file=stderr)
        exit(1)
    else:
        exit(0)
