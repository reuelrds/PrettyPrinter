# Begin -- Parse tree node strategy for printing the special form begin

import sys

from Special import Special


class Begin(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.

        if n > 0:
            sys.stdout.write("\n")

        sys.stdout.write(' ' * n)
        sys.stdout.write("(begin")

        t.getCdr().print(n=(abs(n)+4), p=True)
