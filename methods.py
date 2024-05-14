#Numerical methods functions.
#Linear Systems: GaussJordan, GaussJacobi
#All Systems: Newton

import numpy as np
from util import *

"""""
Auxiliary function of methodGaussJordan

if a line has a zero on its pivots, it needs to be changed with
another one that wont lead to a zero on both lines pivot position
"""
def permutateLine(line_num, system, system_dimension):
    for i in range(0, system_dimension):
        if (i == line_num):
            continue
        if(system[i][line_num] != 0) and (system[line_num][i] != 0):
            print("Permutating lines {0} and {1}".format(i, line_num))
            aux_line = tuple(system[i])
            system[i] = system[line_num]
            system[line_num] = aux_line
            return system
    return []

"""""
Direct method, coverts the argumented matrix into the row echelon form
Note that this functions can only compute derivatives of polynomials


Parameters: system_unsolved: array<array<float>[n][n+1]}, containing the polynomials of each term
Return values: sol[n], an list with the solution of the system
               [], an empty list indicating that no solution could be found
"""
def methodGaussJordan(system_unsolved):
    system = np.asarray(system_unsolved)
    system_dimension = len(system)
    
    for n in range(0, system_dimension):

        #determining current pivot and checking if lines need to be permutated
        print("Using Pivot a{0}{0} = {1:.2f}".format(n+1, system[n][n]))
        pivot = system[n][n]
        if(pivot == 0):
            system = permutateLine(n, system, system_dimension)

        #no valid line permutations found, system has no or inifinite solutions
        if(len(system) == 0):
            return []

    
        #subtractes every line (that is  not the pivot line) by the "line_pivot"(a[line][pivot_collumn]) diveded by the pivot value
        #Ln = Ln - (a[n][pivot_collumn])* Lpivot
        print()
        print("1.{} Subtracting line by line_pivot/pivot * pivot_line".format(n+1))
        for i in range(0, system_dimension):
            if(i != n):
                line_pivot = float(system[i][n]/pivot)
                for j in range(0, system_dimension+1):
                    system[i][j] = float(system[i][j] - line_pivot*system[n][j])
        
        printSystem(system)

    print("2. Normalizing the system: ")
    

    #divides the line by the pivot value
    sol = []
    for i in range(0, system_dimension):
        normalizator = system[i][i]
        for j in range(0, system_dimension+1):
            system[i][j] = system[i][j]/normalizator
            if(j == system_dimension):
                sol.append(system[i][j])
        
    printSystem(system)
    return tuple(sol)



"""""
Iterative method used for linear systems
Parameters: system_unsolved, array<float>[n][n+1], where the last collumn is b
            wanted_error, float indicating the minimum error acceptable
Return values: X[n], indicating the approximate solutions found for the given system
"""
def methodGaussJacobi(system_unsolved, wanted_error):
    flag = True
    count = 1
    system = np.asarray(system_unsolved)
    b = []
    while(flag):
        print("----- GAUSS-JACOBI ITERATION {} -----".format(count))

        #mouting the A and g matrices
        if(count == 1):
            A = []  
            g = []

            
            for i in range(len(system)):
                line = []
                for j in range(len(system)):
                    if(i == j):
                        line.append(0)
                        b.append(system[i][-1]/system[i][i])
                    else:
                        line.append((-1)*system[i][j]/system[i][i])
                A.append(line)
            
            max_b = 0
            for i in b:
                if (abs(i) > max_b):
                    max_b = abs(i)
            g = b

        #calculating new X aproximations
        X = []
        for i in range(len(system)):
            value = 0
            for j in range(len(system)):
                value += A[i][j]*g[j]
            value += b[i]
            X.append(value)
        x_string = "Aproximations of X after {} iterations: [".format(count)
        for i in range(len(X)):
            x_string += "{:.2f}".format(X[i])
            if (i != len(X)-1):
                x_string += ", "
        print(x_string + "]")

        #checking for max error value:
        error = 0
        for i in range(len(X)):
            if (abs((X[i] - g[i]))/max_b) > error:
                error = abs(X[i] - g[i])/max_b
        
        if (error <= wanted_error):
            print("Maximum Error = {:.5f}, less then wanted error = {:.2f}, stopping".format(error, wanted_error))
            return X
        else:
            print("Maximum Error = {:.5f}, bigger then wanted error = {:.2f}, continuing".format(error, wanted_error))
            g = X
            count += 1



""""
Iterative method used for gerneric systems

Parameters: system_unsolved, array<float>[n][n+1], where the last collumn is b
            wanted_error, float indicating the minimum error acceptable
            initial_guess, float[n] indicating the initial guess made
Return values: solution/guess[n], the approximate solution found by the function

"""
def methodNewton(system_unsolved, wanted_error, initial_guess):
    system = system_unsolved
    count = 1
    jacobian = []
    F = []
    flag = True
    guess = initial_guess
    while(flag):
        print("----- NEWTON ITERATION {} -----".format(count))
        guess_print = "Evaluating initial guess at the jacobian for guess = ["
        for i in range(len(guess)):
            guess_print += "{:.2f}".format(guess[i])
            if(i != len(guess)-1):
                guess_print += ", "
        print(guess_print + "]")

        #mouting the F and jacobian matrices
        if(count == 1):
            for i in range(len(system)):
                line_jacobian = []
                line_F = []
                for j in range(len(system)):
                    polynomial = np.poly1d(system[i][j])
                    line_F.append(polynomial)
                    derrivative = polynomial.deriv()
                    line_jacobian.append(derrivative)
                line_F.append(system[i][-1])
                jacobian.append(line_jacobian)
                F.append(line_F)
            

        #mouting the S matrix (F(X))
        S = []
        for i in F:
            s_value = 0
            for j in range(len(i)-1):
                s_value += i[j](guess[j])
            s_value -= i[-1]
            S.append(float(s_value))

        #checking for max S error
        max_s_value = 0
        for i in range(len(S)):
            if (abs(S[i]) > max_s_value):
                max_s_value = abs(S[i])
        #stop condition 1
        if(max_s_value < wanted_error):

            return guess

        #mounts the new system found through jacobian(s) = -F(X)
        new_sys = []
        for i in range(len(system)):
            line = []
            for j in range(len(system)):
                line.append(jacobian[i][j](guess[j]))
            line.append(-S[i])
            new_sys.append(line)

        #solving this linear system through Gauss-Jacobi method
        printSystem(new_sys)
        print("Solving intermediary system through Gauss-Jacobi:")
        print()
        solution = methodGaussJacobi(new_sys, 0.01)
        print()

        #evaluating new solutions
        for i in range(len(solution)):
            solution[i] = guess[i] + solution[i]

        #finding error values of new solutions
        error = 0
        for i in range(len(solution)):
            if(abs(guess[i] + solution[i]) > error):
                error = abs(guess[i] - solution[i])
        
        #stop condition 2
        if (error <= wanted_error):
            print("Maximum Error = {:.5f}, less then wanted error = {:.2f}, stopping".format(error, wanted_error))
            return tuple(solution)
        else:
            print("Maximum Error = {:.5f}, bigger then wanted error = {:.2f}, continuing".format(error, wanted_error))
            print()
            guess = solution
            count += 1


