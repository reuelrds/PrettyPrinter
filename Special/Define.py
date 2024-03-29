# Define -- Parse tree node strategy for printing the special form define

import sys

from Special import Special


class Define(Special):

    def __init__(self):
        pass

    def print(self, t, n, p):

        sys.stdout.write(' ' * n)
        sys.stdout.write("(define ")

        if not t.getCdr().getCar().isPair():
            t.getCdr().print(n=-(abs(n)+4), p=True)

            if n >= 0:
                sys.stdout.write("\n")
        else:

            variable_name = t.getCdr().getCar()
            variable_value = t.getCdr().getCdr().getCar()
            end_paren = t.getCdr().getCdr().getCdr()

            variable_name.print(n=-(abs(n) + 4), p=False)

            if abs(n) + 4 > 0:
                sys.stdout.write("\n")

            variable_value.print(n=(abs(n) + 4), p=False)
            end_paren.print(n=(abs(n)+4), p=True)
