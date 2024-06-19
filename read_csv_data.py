"""
Feito por Lucas Louzada Paganoto Moura - 2024
Dúvidas ou sugestões: lucaslpmoura@gmail.com
"""


import csv

"""
Takes an .csv formated as:
"x";x1;x2;x3;...;xn
"value";v1;v2;v3;...;vn
and reads all its values
Arguments: 
    filename - name of the .csv file ("file.csv")
Returns:
    tuple(value_pairs) - an tuple of value pairs ([x, f(x)])
"""
def read_csv_data(filename):
    elements = []
    value_pairs = []
    file = open(filename, newline='')
    csv_reader = csv.reader(file)
    for row in csv_reader:
        element = ""
        for elem in "".join(row):
            if(elem != ";"):
                element = element + elem
            else:
                elements.append(element)
                element = ""
        
        #Needed to add the last element, as it is not ended by ";"
        elements.append(element)

    for i in range (1,(int(len(elements)/2))):
        value_pair = (float(elements[i]), float(elements[i+int(len(elements)/2)]))
        value_pairs.append(value_pair)
    
    """"
    for i in (value_pairs):
        print(i)
    """

    return tuple(value_pairs)