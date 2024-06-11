"""
Feito por Lucas Louzada Paganoto Moura - 2024
Dúvidas ou sugestões: lucaslpmoura@gmail.com
"""

from bissection import *

#Sample application for implemented functions

print("Using bissection method for function: x³ - 9x + 3")

print("1) Isolating Root intervals")

count = 1
for interval in all_root_intervals(f_tst, -10, 10):
    print("Interval {}: [{:.3f}, {:.3f}]".format(count, interval[0], interval[1]))
    count += 1

count = 1
print("2) Applying Bissection method:")

for root in bissection_method(f_tst, 0.0001):
    print("Root {}: {:.3f}".format(count, root))