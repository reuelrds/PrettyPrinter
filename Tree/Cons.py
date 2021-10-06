# Cons -- Parse tree node class for representing a Cons node

import sys

import Special
import Tree


class Cons(Tree.Node):
    def __init__(self, a, d):
        self.car = a
        self.cdr = d
        self.parseList()

    # parseList() `parses' special forms, constructs an appropriate
    # object of a subclass of Special, and stores a pointer to that
    # object in variable form.  It would be possible to fully parse
    # special forms at this point.  Since this causes complications
    # when using (incorrect) programs as data, it is easiest to let
    # parseList only look at the car for selecting the appropriate
    # object from the Special hierarchy and to leave the rest of
    # parsing up to the interpreter.
    def parseList(self):

        if isinstance(self.car, Tree.Ident):

            if self.car.getName() == "begin":
                self.form = Special.Begin()

            elif self.car.getName() == "cond":
                self.form = Special.Cond()

            elif self.car.getName() == "define":
                self.form = Special.Define()

            elif self.car.getName() == "if":
                self.form = Special.If()

            elif self.car.getName() == "lambda":
                self.form = Special.Lambda()

            elif self.car.getName() == "let":
                self.form = Special.Let()

            elif self.car.getName() == "quote":
                self.form = Special.Quote()

            elif self.car.getName() == "set":
                self.form = Special.Set()

            else:
                self.form = Special.Regular()
        else:
            self.form = Special.Regular()

    def print(self, n, p=False):
        self.form.print(self, n, p)
        # sys.stdout.write("(")
        # self.car.print(n=-1)
        # sys.stdout.write(". ")
        # self.cdr.print(n=-1)

        # sys.stdout.write(")")


if __name__ == "__main__":
    c = Cons(Tree.Ident("Hello"), Tree.Ident("World"))
    c.print(0)
