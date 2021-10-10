# If -- Parse tree node strategy for printing the special form if

import sys

from Special import Special


class If(Special):

    def __init__(self):
        pass

    def print(self, t, n, p):


        sys.stdout.write(' ' * n)
        sys.stdout.write("(if ")

        condition = t.getCdr().getCar()
        truthy_expression = t.getCdr().getCdr().getCar()
        falsy_expression = t.getCdr().getCdr().getCdr().getCar()
        end_paren = t.getCdr().getCdr().getCdr().getCdr()


        condition.print(n=-(abs(n)+4), p=False)
        if abs(n) + 4 > 0:
            sys.stdout.write("\n")
        truthy_expression.print(n=(abs(n)+4), p=False)

        falsy_expression.print(n=(abs(n)+4), p=False)

        sys.stdout.write(" " * (abs(n)))
        sys.stdout.write(")")
        
        if abs(n) + 4 > 0:
            sys.stdout.write("\n")
