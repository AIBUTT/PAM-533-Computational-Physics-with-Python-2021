import math
import random
import numpy as np

# USING VARIANCE REDUCTION METHOD, WE ARE INTEGRATING x^2 FROM a TO b WITH KNOWN FUNCTION x
a=0.0;b=5.0;c=(b**2-a**2)/2.0;

def FUNC1(x):
    #return math.pow(x,2)
    return math.pow(x,math.sin(x))
    #return math.sin(x)/x

ENSAMBLE=1
ENSAMBLE_DATA=np.array([]); E_D1=np.array([]);

for k in range(ENSAMBLE):
    N=10
    DATA=np.array([]); D1=np.array([]);
    for i in range(N):
        r1=random.uniform(a,b)
        DATA=np.append(DATA,FUNC1(r1) - r1); D1=np.append(D1,FUNC1(r1)); print(FUNC1(r1), r1, FUNC1(r1)-r1)
    MEAN=np.mean(DATA); M1=np.mean(D1);
    ENSAMBLE_DATA=np.append(ENSAMBLE_DATA,(b-a)*MEAN+c); E_D1=np.append(E_D1,(b-a)*M1);

print(ENSAMBLE_DATA)
print(np.max(ENSAMBLE_DATA))
print(np.mean(ENSAMBLE_DATA))
print(E_D1)
print(np.mean(E_D1))

