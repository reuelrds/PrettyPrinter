# Quote -- Parse tree node strategy for printing the special form quote

import sys

from Special import Special


class Quote(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.


        sys.stdout.write(' ' * n)
        sys.stdout.write("'")

        t.getCdr().getCar().print(n=-(abs(n)), p=False)

        if n > 0:
            sys.stdout.write("\n")
