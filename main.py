from util import *
from methods import methodGaussJordan, methodGaussJacobi
import numpy as np

test_system = ([3.0, 2.0, 4.0, 1.0],
               [1.0, 1.0, 2.0, 2.0],
               [4.0, 3.0, -2.0, 3.0])

test_system1 = ([10.0, 2.0, 1.0, 7.0],
                [1.0, 5.0, 1.0, -8.0],
                [2.0, 3.0, 10.0, 6.0])

#taking the system to be solved from the user
#system = takeSystem()
system = test_system


print("Solving for system: ")
printSystem(system)

solution = methodGaussJordan(system)
if(solution == []):
    print("System could not be solved!")
    exit()



sol_string = "Solution found through Gauss-Jordan method: b = ["
for i in solution:
    add_str = "{:.2f}".format(i)
    sol_string += add_str + ", "
print(sol_string+"]")


system = test_system1
print("Solving for system:")
printSystem(system)
methodGaussJacobi(system, 0.05)

