#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
    av = len(sys.argv) - 1
    if av == 0:
        print("{} arguments.".format(av))
    elif av == 1:
        print("{} argument:".format(av))
    else:
        print("{} arguments:".format(av))
    if av >= 1:
        av = 0
        for i in sys.argv:
            if av != 0:
                print("{}: {}".format(av, i))
            av += 1
