# Lambda -- Parse tree node strategy for printing the special form lambda

import sys
from Special import Special


class Lambda(Special):
    # TODO: Add fields and modify the constructor as needed.
    def __init__(self):
        pass

    def print(self, t, n, p):

        sys.stdout.write(' ' * n)
        sys.stdout.write("(lambda ")

        # THe variable names are from the function syntax
        # at https://www.cs.cmu.edu/Groups/AI/html/r4rs/r4rs_6.html

        formals = t.getCdr().getCar()
        body = t.getCdr().getCdr().getCar()
        end_paren = t.getCdr().getCdr().getCdr()

        formals.print(n=-(abs(n)+4), p=False)
        if abs(n) + 4 > 0:
            sys.stdout.write("\n")
        body.print(n=(abs(n)+4), p=False)
        
        sys.stdout.write(" " * (abs(n)))
        sys.stdout.write(")")
        
        sys.stdout.write("\n")
