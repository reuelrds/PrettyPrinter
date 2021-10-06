# If -- Parse tree node strategy for printing the special form if

import sys

from Special import Special


class If(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):
        # TODO: Implement this function.

        sys.stdout.write(' ' * n)
        sys.stdout.write("(if ")

        # TODO: Handle the case when getCar and getCdr return `None`.
        condition = t.getCdr().getCar()
        truthy_expression = t.getCdr().getCdr().getCar()
        falsy_expression = t.getCdr().getCdr().getCdr().getCar()

        if condition:
            condition.print(n=-(n+4), p=False)

        sys.stdout.write("\n")

        if truthy_expression:
            sys.stdout.write(' ' * (n + 4))
            truthy_expression.print(n=-(n+4), p=False)

        sys.stdout.write("\n")
        if falsy_expression:
            sys.stdout.write(' ' * (n + 4))
            falsy_expression.print(n=-(n+4), p=False)

        sys.stdout.write("\n")
        sys.stdout.write(")")
