import sympy as sym
import numpy as np
x = sym.symbols('x')
p = sym.Poly(x**2)
r = np.poly1d([1,2,3,4,5,6,7])
print(r)
#print(p)
