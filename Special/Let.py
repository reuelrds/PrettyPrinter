# Let -- Parse tree node strategy for printing the special form let

import sys

from Special import Special


class Let(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):

        if n > 0:
            sys.stdout.write("\n")

        sys.stdout.write(' ' * n)
        sys.stdout.write("(let")

        t.getCdr().print(n=(abs(n)+4), p=True)


