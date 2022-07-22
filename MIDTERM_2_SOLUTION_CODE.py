#MIDTERM_2 SOLUTION
import math
import numpy as np
import scipy

#DIFFERENT FUNCTIONS
F1=lambda x: (10.0/x)*math.sin(x)
F2=lambda x: (10.0/pow(x,2.0))*math.cos(x)
F3=lambda x: (10.0/pow(x,2.0))*math.sin(x)*math.cos(x)
RANGE_V=lambda V: math.pow(V,2)*math.sin(2.0*math.pi/8.0)/9.8
RANGE_T=lambda T: math.pow(50.0,2)*math.sin(2.0*T)/9.8

#ROOTS
print("ROOTS")
from scipy.optimize import bisect
R1 = bisect(F1, 6, 7, xtol=1e-6, full_output=True)
R2 = bisect(F2, 7, 8, xtol=1e-12, full_output=True)
R3 = bisect(F3, -2, -4, xtol=1e-18, full_output=True)

print(R1); print(R2); print(R3)

#INTEGRATION
print("INTEGRATION")
from scipy.integrate import simpson
x=np.linspace(0.5*math.pi,3.0*math.pi,10)
Y1=(10.0/x)*np.sin(x)
Y2=(10.0/x**2.0)*np.cos(x)
Y3=(10.0/x**2.0)*np.sin(x)*np.cos(x)
I1F=simpson(Y1,x,even='first'); I1L=simpson(Y1,x,even='last')
I2F=simpson(Y2,x,even='first'); I2L=simpson(Y2,x,even='last')
I3F=simpson(Y3,x,even='first'); I3L=simpson(Y3,x,even='last')

print("{:5.4f}".format(abs(I1F-I1L))); print("{:5.4f}".format(abs(I2F-I2L))); print("{:5.4f}".format(abs(I3F-I3L)))

#DIFFERENTIATION
print("DIFFERENTIATION")
from scipy.misc import derivative
R_V=derivative(RANGE_V, 50, dx=0.2, n=1, order=7) #dx=0.1|0.2
R_T=derivative(RANGE_T, math.pi/8, dx=math.pi/180, n=1, order=7) #dx=math.pi/360|math.pi/180
dR=R_V*0.2+R_T*math.pi/180

print("{:5.4f}".format(dR))

