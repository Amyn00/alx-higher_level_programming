#!/usr/bin/python3
if __name__ == "__main__":
    """Print the addition of all args."""
    import sys
    result = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            result += int(arg)
    print(result)
