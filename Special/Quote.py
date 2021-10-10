# Quote -- Parse tree node strategy for printing the special form quote

import sys

from Special import Special


class Quote(Special):

    def __init__(self):
        pass

    def print(self, t, n, p):

        sys.stdout.write(' ' * n)
        sys.stdout.write("'")

        t.getCdr().getCar().print(n=-(abs(n)), p=False)

        if n > 0:
            sys.stdout.write("\n")
