# Regular -- Parse tree node strategy for printing regular lists

import sys

from Special import Special


class Regular(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.

        car = t.getCar()
        cdr = t.getCdr()

        # if t.isPair():

        sys.stdout.write(" " * n)

        if not p:
            sys.stdout.write("(")

        elif n < 0:
            sys.stdout.write(" ")

        if car.isPair():

            car.print(-(abs(n)), False)

        else:
            car.print(-(abs(n)), True)

        cdr.print(-(abs(n)), True)

        # TODO: Handle Dot
        # else:
        # car.print(-(abs(n)), True)

        # if cdr.isNull() or cdr.isPair():
        # else:
        # cdr.print(-abs(n+4), False)

        c = 1

        # if n > 0:
        # sys.stdout.write("\n")
