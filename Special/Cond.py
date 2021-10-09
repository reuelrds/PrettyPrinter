# Cond -- Parse tree node strategy for printing the special form cond

import sys

from Special import Special


class Cond(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):


        sys.stdout.write(' ' * n)
        sys.stdout.write("(cond")

        t.getCdr().print(n=(abs(n)+4), p=True)

        if n > 0:
            sys.stdout.write("\n")