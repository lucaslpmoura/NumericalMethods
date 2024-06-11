"""
Feito por Lucas Louzada Paganoto Moura - 2024
Dúvidas ou sugestões: lucaslpmoura@gmail.com
"""

from root_interval import *

"""
Bissection method used for find all real roots of a function from its root intervals
Arguments:
    function - the function to be used
    error - the accepted error
Returns:
    [a,b,c...] - returns all the real roots found inside the intervals
"""

def bissection_method(function, error):
    intervals = all_root_intervals(function, -10, 10)
    roots = []
    for interval in intervals:
        if interval[1] - interval[0] <= error:
            roots.append((interval[1] - interval[0])/2)
        else:
            M = function(interval[0])
            x = (interval[1] - interval[0])/2
            if M*function(x) > 0:
                roots.append(interval[0])
            else:
                roots.append(interval[1])
    return roots
