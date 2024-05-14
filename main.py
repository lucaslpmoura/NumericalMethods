from util import *
from methods import methodGaussJordan, methodGaussJacobi, methodNewton
import numpy as np

def printMenu():
    print("------------------------------------")
    print("Select an method to use or press 'q' to quit: ")
    print("1) Gauss-Jordan")
    print("2) Gauss-Jacobi")
    print("3) Newton")
    print("------------------------------------")



test_system_newton=([[-1,0,4,0], [1,0], [0]],
              [[-1/9,0,0], [-1/4,1,0], [-1]])

test_system_direct=([2.0,2.0,1.0,1.0,7.0],
              [1.0,-1.0,2.0,-1.0,1.0],
              [3.0,2.0,-3.0,-2.0,4.0],
              [4.0,3.0,2.0,1.0,12.0])

test_system_iterative=([5.0,2.0,-1.0,4.0,12.0],
                    [2.0,6.0,2.0,-1.0,10.0],
                    [1.0,2.0,7.0,3.0,17.0],
                    [3.0,-1.0,2.0,8.0,11.0])

clearScreen()
while(True):
    printMenu()
    op = input()
    match(op):
        case "q":
            exit()
        case "Q":
            exit()
        case "1":
            clearScreen()
            print("Resolving system through Gauss-Jordan method: ")
            printSystem(test_system_direct)
            solution = methodGaussJordan(test_system_direct)
            if(len(solution) == 0):
                print("No solution could be found for the system!")
            else:
                print("Solution = " + solutionToString(solution))
            print()
            cnt = input("Press any key to return to the menu.")
            clearScreen()


        case "2":
            clearScreen()
            print("Resolving system through Newton's method, using error = 0.01: ")
            printSystem(test_system_iterative)
            solution = methodGaussJacobi(test_system_iterative, 0.01)
            if(len(solution) == 0):
                print("No solution could be found for the system!")
            else:
                print("Solution = " + solutionToString(solution))
            print()
            cnt = input("Press any key to return to the menu.")
            clearScreen()


        case "3":
            clearScreen()
            print("Resolving system through Gauss-Jacobi method, using error = 0.01, and initial guess [-1,-2]: ")
            print()
            print("See source code for system coeficients.")
            print()
            solution = methodNewton(test_system_newton, 0.01, [-1,-2])
            if(len(solution) == 0):
                print("No solution could be found for the system!")
                
            else:
                print("Solution = " + solutionToString(solution))
            print()
            cnt = input("Press any key to return to the menu.")
            clearScreen()


        case _:
            print("Please enter an valid option.")
