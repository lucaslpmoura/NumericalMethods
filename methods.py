import numpy as np
from util import *

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

def methodGaussJordan(system_unsolved):
    system = np.asarray(system_unsolved)
    system_dimension = len(system)
    
    for n in range(0, system_dimension):
        pivot = system[n][n]
        if(pivot == 0):
            system = permutateLine(n, system, system_dimension)

        if(system == []):
            return system
        
        print("Using Pivot a{0}{0} = {1:.2f}".format(n+1, system[n][n]))
        print()
        print("1.{} Subtracting line by line_pivot/pivot * pivot_line".format(n+1))
        for i in range(0, system_dimension):
            if(i != n):
                line_pivot = system[i][n]/pivot
                for j in range(0, system_dimension+1):
                    system[i][j] -= line_pivot*system[n][j]
        
        printSystem(system)

    print("2. Normalizing the system: ")
    
    sol = []
    for i in range(0, system_dimension):
        normalizator = system[i][i]
        for j in range(0, system_dimension+1):
            system[i][j] = system[i][j]/normalizator
            if(j == system_dimension):
                sol.append(system[i][j])
        
    printSystem(system)
    return tuple(sol)


def methodGaussJacobi(system_unsolved, wanted_error):
    flag = True
    count = 1
    system = np.asarray(system_unsolved)
    b = []
    while(flag):
        print("----- ITERATION {} -----".format(count))
        if(count == 1):
            A = []  
            g = []
            #mouting the A and g matrixes
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
            print("Maximum Error = {:.2f}, less then wanted error = {:.2f}, stopping".format(error, wanted_error))
            return X
        else:
            print("Maximum Error = {:.2f}, bigger then wanted error = {:.2f}, continuing".format(error, wanted_error))
            g = X
            count += 1

