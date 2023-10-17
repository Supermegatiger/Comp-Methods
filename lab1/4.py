from math import *
s = lambda n : 1/((n**4)*(n**2+1))

e = 1e-9

ans = 1.07667404746858117413405079475

k = 1
tek = s(k)
res = tek
while abs(res - ans) > e:
    if k%1000000 == 0:
        print(res, abs(res-ans) - e,k)
    k+=1
    tek = s(k)
    if(res+tek==res):
        break
    res += tek
print(f'k = {k}; s = {pi*pi/6 - pi**4/90 + res};')

# 1.076674038454912