# Regular -- Parse tree node strategy for printing regular lists

import sys

from Special import Special


class Regular(Special):

    def __init__(self):
        pass

    def print(self, t, n, p):

        car = t.getCar()
        cdr = t.getCdr()

        sys.stdout.write(" " * n)

        if not p:
            sys.stdout.write("(")

            # Increased indendation to match the output
            # to the reference implementation
            car.print(-(abs(n) + 4), False)

            if not cdr.isNull():
                sys.stdout.write(" ")

            if cdr.isPair() or cdr.isNull():
                cdr.print(-(abs(n)), True)

            else:
                sys.stdout.write(". ")
                cdr.print(-(abs(n)), True)

                sys.stdout.write(")")

            if n >= 0:
                sys.stdout.write("\n")
        else:

            # Used by the print method for lambda class
            indent = car.print(-(abs(n)), False)

            if not cdr.isNull():
                sys.stdout.write(" ")
            if n > 0 and not indent:
                sys.stdout.write("\n")

            if cdr.isPair() or cdr.isNull():
                cdr.print(n, p)

            else:
                sys.stdout.write(". ")
                cdr.print(-(abs(n)), True)
                sys.stdout.write(")")
