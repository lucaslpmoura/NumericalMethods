
def printSystem(system):
    system_dimension = len(system)
    print()
    for i in range(0, system_dimension):
        line_to_print = "| "
        for j in range(0, system_dimension):
            if(system[i][j] < 0) and (j == 0):
                line_to_print += "-"

            line_to_print += "{0:.2f} * x{1}".format(abs(system[i][j]), j+1)

            if(j != system_dimension-1) and (system[i][j+1] < 0):
                line_to_print += " - "
            elif(j != system_dimension-1):
                line_to_print += " + "


        #adding the "b" collumn
        line_to_print += " = {0:.2f}".format(system[i][-1])
        print(line_to_print)
    print()

def takeSystem():
    system_dimension = int(input("Please enter the system dimension (max 6): "))
    system = []
    count = 0
    for i in range(0, system_dimension):
        system_line = []
        for j in range(0, system_dimension):
            system_line.append(float(input("Element a{0}{1}: ".format(i+1, j+1))))
        system_line.append(float(input("Element b{0}: ".format(i+1))))
        system.append(system_line)
    
    system = tuple(system)
    return system