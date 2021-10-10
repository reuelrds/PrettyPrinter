# Scheme Pretty Printer
*By Xinyue Yu and Reuel D'silva for CSC 4101 Programming Languages Course.*

The Scheme Pretty Printer takes in a scheme expression and pretty-prints it back to the console.

\
&nbsp;

## Project Specific details

We have left factored the grammar by introducing a new non-terminal ***rest'*** after converting it into BNF form.

The pretty printing for each of the tokens and special form objects is implemented into their respective print method. We followed Dr Baumgartner's suggestion to use the indendation parameter to recognize when the pretty printer needs to print a newline _(i.e. when the indendation is negative, the program does not print a newline, and when it is positive, it prints a new line)_.

The tests.scm file in the project root contains a set of test cases that we used to test our implementation. The outputs of these test cases matches the output of the reference implementation.


## To run the Program
```python
python3 SPP.py
```

