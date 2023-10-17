import math

def result(m, c, t, b):
    f = (m*math.tan(t)+abs(c*math.sin(t)))**(1/3)
    z = m*math.cos(b*t*math.sin(t))+c
    return f'F: {f}\nZ: {z}'

m=2
c=-1
t=1.2
b=0.7

print(result(m, c, t, b))
