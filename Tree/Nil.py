# Nil -- Parse tree node class for representing the empty list

import sys
from Tree import Node


class Nil(Node):
    __instance = None

    @staticmethod
    def getInstance():
        if Nil.__instance == None:
            Nil()
        return Nil.__instance

    def __init__(self):
        if Nil.__instance != None:
            raise Exception("Class Nil is a singleton")
        else:
            Nil.__instance = self

    def print(self, n, p=False):


        sys.stdout.write(' ' *( n - 4 ))

        if p:
            sys.stdout.write(")")
        else:
            sys.stdout.write("()")

        if n > 0:
            sys.stdout.write("\n")

    def isNull(self):
        return True


if __name__ == "__main__":
    n = Nil.getInstance()
    n.print(0)
