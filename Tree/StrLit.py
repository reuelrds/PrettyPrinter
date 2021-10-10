# StLit -- Parse tree node class for representing string literals

import sys
from Tree import Node


class StrLit(Node):
    def __init__(self, s):
        self.strVal = s

    def print(self, n, p=False):


        sys.stdout.write(' ' * n)

        sys.stdout.write("\"" + self.strVal + "\"")
        if n > 0:
            sys.stdout.write("\n")

    def isString(self):
        return True


if __name__ == "__main__":
    id = StrLit("foo")
    id.print(0)
