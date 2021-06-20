# This program is meant for me as a refresher of linear algebra and an oportunity to code more
# What it does, it plays around with the properties of the straight line

import matplotlib.pyplot as plt
import numpy as np

class LinearEquation:
    def __init__(self, a, b, c):
        """Class constructor, a, b and c are coefficients of a linear equation"""

        self.a = a
        self.b = b
        self.c = c

        # Calculate slope
        self.slope = (-1 * self.a) / self.b

        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c,(int, float)):
            raise TypeError('Coeffiecient must be numerical')
      
    def __str__(self):
        if self.b < 0 or self.c < 0:
            return f'y = {self.a/self.b:.2f}x - {abs(self.c/self.b):.2f}'
        return f'y = {self.a/self.b:.2f}x + {self.c/self.b:.2}'

class LinearEquationSystem:
    def __init__(self, equation1, equation2):
        '''Class constructor. Creates a linear equation system of 2x2'''
        self.equation1 = equation1
        self.equation2 = equation2

        if not isinstance(self.equation1, LinearEquation) or not isinstance(equation2, LinearEquation):
            raise TypeError('Enter a linear equation')
        
    def solve(self):
        """Returns the ordered pair P(x, y) the satisfies both equations of the system"""
        # According to the general solution for 2x2 equation systems, a system has a unique solution if and only if
        # a11a22 - a12a21 != 0
        denominator = (self.equation1.a * self.equation2.b) - (self.equation1.b * self.equation2.a)
        
        # If a11a22 - a12a21 == 0, the system has either no solution of infinate solutions
        if denominator == 0:
            return (None, None) 
        
        x = ((self.equation2.b * self.equation1.c) - (self.equation1.b * self.equation2.c)) / denominator
        y = (-(self.equation1.a / self.equation1.b) * x) + (self.equation1.c/self.equation1.b)

        return (x, y)
    
    def to_list(self):
        return [self.equation1, self.equation2]

    def __str__(self):
        if self.equation1.b < 0:
            return f'{self.equation1.a}x - {abs(self.equation1.b)}y = {self.equation1.c}\n{self.equation2.a}x + {self.equation2.b}y = {self.equation2.c}'
        elif self.equation2.b < 0:
            return f'{self.equation1.a}x + {self.equation1.b}y = {self.equation1.c}\n{self.equation2.a}x - {abs(self.equation2.b)}y = {self.equation2.c}'
        elif self.equation1.b < 0 and self.equation2.b < 0:
            return f'{self.equation1.a}x - {abs(self.equation1.b)}y = {self.equation1.c}\n{self.equation2.a}x - {abs(self.equation2.b)}y = {self.equation2.c}'
        else:
            return f'{self.equation1.a}x + {self.equation1.b}y = {self.equation1.c}\n{self.equation2.a}x + {self.equation2.b}y = {self.equation2.c}'


def draw(equation_system, start=-100, stop=100):
    """Draws all equations on the same figure"""

    if not isinstance(equation_system, LinearEquationSystem):
        raise TypeError('No LinearEquationSytem given')

    # Create figure
    x = np.arange(start, stop)
    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot(111)
    ax.grid(True, linewidth=0.5, linestyle=':')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    for equation in equation_system.to_list():
        y = (equation.slope * x) + (equation.c / equation.b)
        ax.plot(x, y, label=equation)

    # Solve equation system
    p, q = equation_system.solve()
    if p is None and q is None:
        result = 'No solution'

    else:
        result = f'Solution at P({p:.2f}, {q:.2f})'
        ax.text(p, q, f'P({p:.2f}, {q:.2f})', size=15)
    
    ax.set_title(f'Linear equations.\n{result}')
    plt.legend()
    plt.show()

