# Parser -- the parser for the Scheme printer and interpreter
#
# Defines
#
#   class Parser
#
# Parses the language
#
#   exp  ->  ( rest
#         |  #f
#         |  #t
#         |  ' exp
#         |  integer_constant
#         |  string_constant
#         |  identifier
#    rest -> )
#         |  exp+ [. exp] )
#
#
#    rest -> )
#         |  exp rest
#         |  exp . exp )
#
#
#    rest -> )
#         |  exp rest'
#
#    rest'-> . exp )
#         |  rest
#
#
#
# and builds a parse tree.  Lists of the form (rest) are further
# `parsed' into regular lists and special forms in the constructor
# for the parse tree node class Cons.  See Cons.parseList() for
# more information.
#
# The parser is implemented as an LL(0) recursive descent parser.
# I.e., parseExp() expects that the first token of an exp has not
# been read yet.  If parseRest() reads the first token of an exp
# before calling parseExp(), that token must be put back so that
# it can be re-read by parseExp() or an alternative version of
# parseExp() must be called.
#
# If EOF is reached (i.e., if the scanner returns None instead of a token),
# the parser returns None instead of a tree.  In case of a parse error, the
# parser discards the offending token (which probably was a DOT
# or an RPAREN) and attempts to continue parsing with the next token.

import sys

import Tree

from Tokens import TokenType
from Tokens import Token


class Parser:
    def __init__(self, s):
        self.scanner = s

    def parseExp(self):
        return self.__parseExp(self.scanner.getNextToken())

    def __parseExp(self, token: Token):
        # TODO: write code for parsing an exp

        # End of input
        if token is None:
            return

        elif token.getType() == TokenType.LPAREN:
            return self.parseRest()

        elif token.getType() == TokenType.TRUE:
            return Tree.BoolLit(True)

        elif token.getType() == TokenType.FALSE:
            return Tree.BoolLit(False)

        elif token.getType() == TokenType.QUOTE:
            return Tree.Cons(Tree.Ident("quote"), Tree.Cons(self.parseExp(), Tree.Nil()))

        elif token.getType() == TokenType.INT:
            return Tree.IntLit(token.getIntVal())

        elif token.getType() == TokenType.STR:
            return Tree.IntLit(token.getStrVal())

        elif token.getType() == TokenType.IDENT:
            return Tree.Ident(token.getName())

        elif token.getType() == TokenType.DOT:
            self.__error("Illegal DOT in the expression")

        elif token.getType() == TokenType.RPAREN:
            self.__error("Illegal Right Parenthesis in the expression")

        else:
            self.__error("Error in parsing token from the input")

    def parseRest(self):
        return self.__parseRest(self.scanner.getNextToken())

    def __parseRest(self, token: Token):
        # TODO: write code for parsing a rest

        # Do we need to test this case in parseRest?
        if token is None:
            return

        elif token.getType() == TokenType.RPAREN:
            return Tree.Nil()

        else:
            car = self.__parseExp(token)
            cdr = self.parseRestPrime()

            if cdr is None:
                self.__error("Error in parsing token from the input")
                return

            else:
                return Tree.Cons(car, cdr)

    # TODO: Add any additional methods you might need

    def parseRestPrime(self):
        token = self.scanner.getNextToken()

        if token is None:
            return

        elif token.getType() == TokenType.DOT:

            car = self.parseExp()
            token = self.scanner.getNextToken()

            if token is None:
                return

            elif token.getType() == TokenType.RPAREN:
                return Tree.Cons(car, Tree.Nil())

            else:
                self.__error("Error in parsing token from the input")
                return

        else:
            return self.__parseRest(token)

    def __error(self, msg):
        sys.stderr.write("Parse error: " + msg + "\n")
