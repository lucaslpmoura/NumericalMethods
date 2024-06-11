"""
Feito por Lucas Louzada Paganoto Moura - 2024
Dúvidas ou sugestões: lucaslpmoura@gmail.com
"""



"""
Finds an interval where an root for the function can be found.
Arguments: 
    function - real function to be tested
    a - lower bound of search
    b - upper bound of search
Returns:
    [] if no interval is found
    [c,d] if an interval is found
"""  


def root_interval(function, a, b):
    step = 0.01 #step used to iterate over interval
    i = float(a)
    while i < float(b):
        if function(a) * function(i+step) <= 0:
            return [i, i+step]
        i += step
        
    return []

"""
Iterates over function, finding all valid root intervals
Arguments: 
    function - real function to be tested
    a - lower bound of search
    b - upper bound of search
Returns:
    [] if no intervals are found
    [[c,d], [e,f], [g,h]...] if at least one valid interval is found
"""

def all_root_intervals(function, a,b):
    all_intervals = []
    interval = [0,0]
    while interval != []:
        interval = root_interval(function, a, b)
        if interval == []:
            break
        all_intervals.append(interval)
        a = interval[1]
    return all_intervals
    
def f_tst(x):
    return x**3 - 9*x + 3


def test_root_interval():
    print(all_root_intervals(f_tst, -10, 10))