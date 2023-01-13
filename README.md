# NEWLANG

This is a simple stack-based interpreter that is capable of performing basic arithmetic operations such as addition and subtraction, as well as handling variables.

The interpreter takes in a file called "prog.nl" as input, which contains a list of operations to be executed. The file can contain the following operations:

* `push(x)`: pushes the value of x onto the stack
* `plus():`pops the last two values from the stack, adds them together, and pushes the result onto the stack
* `minus():`pops the last two values from the stack, subtracts the second popped value from the first, and pushes the result onto the stack
* `dump():`pops the last value from the stack and prints it
* `print(string)`: prints the string
* `set(var,` value): sets the value of the variable
* `get(var)`: gets the value of the variable and pushes it onto the stack

The interpreter also has the ability to skip lines starting with "//", which are treated as comments.

The function `simulate_program(program)` takes in the program as input and executes the operations. The function `compileProgram(program)` is not implemented in this version.

To run the interpreter, simply run the script with a properly formatted "prog.nl" file in the same directory.

## NOTE

----
This README is written with ChatGPT.
