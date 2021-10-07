# IntLit -- Parse tree node class for representing integer literals

import sys
from Tree import Node


class IntLit(Node):
    def __init__(self, i):
        self.intVal = i

    def print(self, n, p=False):

        if n > 0:
            sys.stdout.write("\n")

        sys.stdout.write(' ' * n)

        sys.stdout.write(str(self.intVal))

        # If the indentation value `n` is negative
        # we print a single space after `#t` or `#f`.
        #
        # And if the indentation is positive, we do
        # not print a space.
        #
        # TODO: Explain the following in a better way.
        #       And maybe refactor it to a helper funtion.
        # if n < 0:
        # sys.stdout.write(" " * (-n//n))

        # if n > 0:
        # sys.stdout.write("\n")

    def isNumber(self):
        return True


if __name__ == "__main__":
    id = IntLit(42)
    id.print(0)
