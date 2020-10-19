"""
This module is used for finding solutions to System of Linear Equations
"""

import re
import sympy as sym

def __extract_symbols(equations):
    """Identifies the symbols present in the list of equations and returns them

    equations: A list of equations (strings)

    Returns a List of symbols present in equations_list
    """
    symbols = []
    for equation in equations:
        symbols = symbols + re.findall('[a-zA-Z][a-zA-Z0-9]*', equation)
    symbols = list(set(symbols))
    for i in range(len(symbols)):
        exec(f"symbols[{i}]=sym.Symbol('{symbols[i]}')")
    return symbols

def __solve(equations, symbols):
    """
    This function solves a system of linear equations

    equations: List of equations to be solved
    symbols: Symbols or variables present in the equations

    Returns the solution
    """
    return sym.solve(tuple(equations), tuple(symbols))

def solve_equations():
    """This function is the entry point of this module. It performs following operations:
        1. Asks user for a System of Linear Equations
        2. Finds the solutions for the user input if exists
        3. Gives the solutions or error message to the user
    """
    n = int(input("Enter the number of equations : "))
    print(f"Enter {n} equations")
    equations = [input() for i in range(n)]

    symbols = __extract_symbols(equations)
    if len(symbols) != n:
        print("Number of variables must be equal to number of equations")
        return
    
    try:
        result = __solve(equations, symbols)
    except Exception as error:
        print("Invalid equations. Check your equations and try again")
        return

    for item in result.items():
        print(f"{item[0]} = {item[1]}")