import math

m=2
c=-1
t=1.2
b=0.7
f = (m*math.tan(t)+abs(c*math.sin(t)))**(1/3)
z = m*math.cos(b*t*math.sin(t))+c

print(f'F: {f}\nZ: {z}')
