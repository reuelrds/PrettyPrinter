# Ident -- Parse tree node class for representing identifiers

import sys
from Tree import Node


class Ident(Node):
    def __init__(self, n):
        self.name = n

    def getName(self):
        return self.name

    def print(self, n, p=False):

        sys.stdout.write(' ' * n)

        sys.stdout.write(self.name)

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

    def isSymbol(self):
        return True


if __name__ == "__main__":
    id = Ident("foo")
    id.print(0)
