#!/usr/bin/env python3
from libs import strings
from libs import func_helpers
iota_counter = 0
def iota(reset=False):
    global iota_counter
    if reset:
        iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result


OP_PUSH=iota(True) # pushes to stack
OP_PLUS=iota()     # plus n
OP_MINUS=iota()    # minus n
OP_PRINT=iota()    # prints
OP_DUMP=iota()     # dumps stack
OP_SET=iota()      # Sets var
OP_GET=iota()      # Gets var
OP_DEF=iota()      # Sets function
OP_CALL=iota()     # Gets function
COUNT_OPS=iota()   # op count

def op_push(x):
    return (OP_PUSH, x)
def op_plus():
    return (OP_PLUS,)
def op_minus():
    return (OP_MINUS,)
def op_dump():
    return (OP_DUMP,)
def op_print(string):
    return (OP_PRINT,string)
def op_set(var,value):
    return (OP_SET, var, value)
def op_get(var):
    return (OP_GET, var)
def op_def(name,body):
    return (OP_DEF, name, body)
def op_call(name):
    return (OP_CALL, name)


functions = {} # Stores functions
def simulate_program(program):
    stack = [] 
    variables = {} # stores variables
    for op in program:
        assert COUNT_OPS == COUNT_OPS, "exhaustive handling of operations in simulation"
        if op[0] == OP_PUSH:
            stack.append(op[1])
        elif op[0] == OP_PLUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif op[0] == OP_MINUS:
            a = stack.pop()
            b = stack.pop()
            stack.append(a-b)
        elif op[0] == OP_PRINT:
            print(op[1])
        elif op[0] == OP_DUMP:
            a = stack.pop()
            print(a)
        elif op[0] == OP_SET:
            variables[op[1]] = op[2]
        elif op[0] == OP_GET:
            stack.append(variables.get(op[1], None))  # get the value of the variable, and push None if the variable is not defined
        elif op[0] == OP_DEF:
            print("hit def")
            # Store the function in the dictionary
            functions[op[1]] = op[2]
        elif op[0] == OP_CALL:
            print("hit call")
            # Get the function from the dictionary and execute it
            func = functions.get(op[1], None)
            if func is not None:
                simulate_program(func)  # execute the function
        else:
            assert False, "unreachable"
def compileProgram(program):
    assert False, "compileProgram not implemented"


#QProgram = [push(34),push(35),plus(),dump(),]
program = []

with open("prog.nl", "r") as f:
    lines = [line.strip() for line in open("prog.nl", "r")]
    for line in lines:
        if strings.is_comment(line):#line.startswith("//"):
            continue # skips line
        if "push" in line:
            try:
                val = int(func_helpers.get_value(line))#int(line.split("(")[1].split(")")[0])
                program.append(op_push(val))
            except ValueError:
                print("Error: Invalid value in input file")
        elif "plus" in line:
            program.append(op_plus())
        elif "minus" in line:
            program.append(op_minus())
        elif "dump" in line:
            program.append(op_dump())
        elif "print" in line:
            val = func_helpers.get_value(line)#line.split("(")[1].split(")")[0]
            program.append(op_print(val))
        elif "set" in line:
            val = func_helpers.get_value(line)#line.split("(")[1].split(")")[0]
            var, value = val.split(",")
            program.append(op_set(var, int(value)))
        elif "get" in line:
            var = func_helpers.get_value(line)#line.split("(")[1].split(")")[0]
            program.append(op_get(var))
        elif "def" in line:
            val = line.split("(")[1].split(")")[0]
            name, body = val.split(" ")
            body = body.split(",")
            function_body = []
            for i in body:
                if "push" in i:
                    try:
                        val = int(i.split("(")[1].split(")")[0])
                        function_body.append(op_push(val))
                    except ValueError:
                        print("Error: Invalid value in input file")
                elif "plus" in i:
                    function_body.append(op_plus())
                elif "minus" in i:
                    function_body.append(op_minus())
                elif "dump" in i:
                    function_body.append(op_dump())
                elif "print" in i:
                    val = i.split("(")[1].split(")")[0]
                    function_body.append(op_print(val))
                elif "set" in i:
                    val = i.split("(")[1].split(")")[0]
                    var, value = val.split(",")
                    function_body.append(op_set(var, int(value)))
                elif "get" in i:
                    var = i.split("(")[1].split(")")[0]
                    function_body.append(op_get(var))
            program.append(op_def(name, function_body))
        elif "call" in line:
            print("call")
            val = line.split("(")[1].split(")")[0]
            if val in functions:
                func = functions.get(val, None)
                simulate_program(func)
            else:
                print(f"Error: Function {val} not defined")


    #program.append(lines)
#print("Current:",program)
#print("Target: ",QProgram)
simulate_program(program)