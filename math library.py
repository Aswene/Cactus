import math

def Y(radi,theta):
    return radi*math.cos(theta*math.pi/180)
def Z(radi,theta):
    return radi*math.sin(theta*math.pi/180)

a1 = 10
a2 = 5
a3 = 2
radi = 4

angle = [i for i in range (181)]
print (angle)
x = [5 for i in range (181)]
print (x)
y = [Y(radi,angle[i]) for i in range (181)]
print (y)
z = [Z(radi,angle[i]) for i in range (181)]
print (z)

theta1 = []
print (theta1)
theta2 = []
print (theta2)
d3 = []
print (d3)

for i in angle:
    theta1.append(math.atan(y[i]/x[i]))
    theta2.append(math.atan((a1-z[i])/(math.sqrt(x[i]**2+y[i]**2))))
    d3.append(((a1-z[i])/(math.sin(-1*theta2[i])))-a3-a2)

theta1_o = 0
theta1_u = 0
theta2_o = 0
theta2_u = 0
d3_o = 0
d3_u = 0

for i in angle:
    if 
