import sys

def readlines() -> list[str]:
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            return f.readlines()
    return sys.stdin.readlines()
