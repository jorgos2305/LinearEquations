# This pprogrmas solves the exercises of the book Linear algebra by Stanley Grossman

import itt
import os
#coefficients of the equations
coeffs = ['a', 'b', 'c']
# Keep count of the equations
eq_count = 1

# Store the enteres coeffiecients
coefficients = []

for _ in range(2): # Do thi loop for every equation, that mean twice
    for c in coeffs: # Do this for a, b, c
        valid_input = False
        while not valid_input: # As long as the input is not a integer keep asking for an input
            try:
                inp = int(input(f'Enter the coefficient "{c}" for Equation {eq_count}:\n'))
                valid_input = True
            except Exception as e: # In case we have a letter ask the user to enter the coffient again
                print(e)
                print('Invalid input. Try again')
                continue
        coefficients.append(int(inp)) # Store value
    os.system('clear')
    eq_count += 1 # Next equation

# Define the two linear equations
equation1 = itt.LinearEquation(coefficients[0], coefficients[1], coefficients[2])
equation2 = itt.LinearEquation(coefficients[3], coefficients[4], coefficients[5])

# Define the Equation System
system = itt.LinearEquationSystem(equation1, equation2)

itt.draw(system)
        
