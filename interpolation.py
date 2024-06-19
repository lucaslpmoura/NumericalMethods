"""
Feito por Lucas Louzada Paganoto Moura - 2024
Dúvidas ou sugestões: lucaslpmoura@gmail.com
"""

from read_csv_data import *
import numpy

#Put the name of the .csv file here
datafile = ""

"""
Interpolates the data of an value pair tuple, giving an function
that can evaluate any value, using LaGrange's method
Arguments: 
    data - an tuple of value pairs containing the know values
Returns:
    P - an evaluating function
"""
def interpolate_polynomial(data):
    x = numpy.array([point[0] for point in data])
    y = numpy.array([point[1] for point in data])
    poly = []

    def L(k, x_val):
        Lk = numpy.ones_like(x_val, dtype=numpy.float64)
        for i in range(len(data)):
            if i != k:
                Lk *= (x_val - x[i]) / (x[k] - x[i])
        return Lk

    def P(x_val):
        P_val = numpy.zeros_like(x_val, dtype=numpy.float64)
        for k in range(len(data)):
            P_val += y[k] * L(k, x_val)
        return P_val
    return P


polynomial = interpolate_polynomial(read_csv_data(datafile))
print("Interpolated polynomial from given data: ")
value_to_be_interpolated = float(input("Type a value to be interpolated: "))
print("F({:.2f}) = {:.4f}".format(value_to_be_interpolated, polynomial(value_to_be_interpolated)))