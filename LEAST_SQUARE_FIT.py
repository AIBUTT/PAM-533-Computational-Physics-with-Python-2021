import math
import numpy as np

def classic_lstsqr(x_list, y_list):
    """ Computes the least-squares solution to a linear matrix equation. """
    N = len(x_list)
    x_avg = sum(x_list)/N
    y_avg = sum(y_list)/N
    var_x, cov_xy = 0, 0
    for x,y in zip(x_list, y_list):
        temp = x - x_avg
        var_x += temp**2
        cov_xy += temp * (y - y_avg)
    slope = cov_xy / var_x
    y_interc = y_avg - slope*x_avg
    return (slope, y_interc)

x=np.array([2.0, 3.0, 5.0, 7.0, 9.0])
y=np.array([4.0, 5.0, 7.0, 10.0, 15.0])

m,c = classic_lstsqr(x,y)

# WHEN x = 10: y = mx + c GIVES:

print("TOTAL ICE CREAMS SOLD: ", m*10+c)
