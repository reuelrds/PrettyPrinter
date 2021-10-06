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

        # sys.stdout.write(self.name + '\n')
        sys.stdout.write(self.name + ' ')

    def isSymbol(self):
        return True


if __name__ == "__main__":
    id = Ident("foo")
    id.print(0)
