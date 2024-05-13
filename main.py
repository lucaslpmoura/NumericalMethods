from util import *
from methods import methodGaussJordan, methodGaussJacobi, methodNewton
import numpy as np

test_system = ([3.0, 2.0, 4.0, 1.0],
               [1.0, 1.0, 2.0, 2.0],
               [4.0, 3.0, -2.0, 3.0])

test_system1 = ([10.0, 2.0, 1.0, 7.0],
                [1.0, 5.0, 1.0, -8.0],
                [2.0, 3.0, 10.0, 6.0])

test_system2 = ([[1,0],[1,0],[3]],
                [[1,0,0],[1,0,0], [9]])
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
for i in range (len(solution)):
    add_str = "{:.2f}".format(solution[i])
    sol_string += add_str
    if(i < len(solution)):
        sol_string += ", "
print(sol_string+"]")


system = test_system1
print("Solving for system:")
printSystem(system)
solution = methodGaussJacobi(system, 0.05)
if(solution == []):
    print("System could not be solved!")
    exit()

sol_string = "Solution found through Gauss-Jacobi method: b = ["
for i in range (len(solution)):
    add_str = "{:.2f}".format(solution[i])
    sol_string += add_str
    if(i < len(solution)):
        sol_string += ", "
print(sol_string+"]")

system = test_system2
methodNewton(system, 0.05, [1,5])

