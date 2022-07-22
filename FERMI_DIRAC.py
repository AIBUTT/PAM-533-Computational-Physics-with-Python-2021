import math
from scipy.optimize import bisect

# PROBLEM 2-6 OF CPwP DOCUMENT :-)

def FD_FUNCT(mu):
    value = math.log(math.pow(math.e,40.0*mu)+1) - math.log(math.pow(math.e,40.0*mu-80.0)+1) - 40.0
    return value

VALUE=bisect(FD_FUNCT, 0.0, 2.0, full_output=True)

print(VALUE)
