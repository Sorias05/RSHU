def ToSec(h, m, s): return (h*60*60+m*60+s)
h1=-1
m1=-1
s1=-1
h2=-1
m2=-1
s2=-1
while(h1 < 0 or h1 > 23): h1=int(input("Input hour of 1 moment (int): "))
while(m1 < 0 or m1 > 59): m1=int(input("Input minutes of 1 moment (int): "))
while(s1 < 0 or s1 > 59): s1=int(input("Input seconds of 1 moment (int): "))
while(ToSec(h1, m1, s1) >= ToSec(h2, m2, s2)):
    while(h2 < 0 or h2 > 23): h2=int(input("Input hour of 2 moment (int): "))
    while(m2 < 0 or m2 > 59): m2=int(input("Input minutes of 2 moment (int): "))
    while(s2 < 0 or s2 > 59): s2=int(input("Input seconds of 2 moment (int): "))
print(ToSec(h2, m2, s2) - ToSec(h1, m1, s1))