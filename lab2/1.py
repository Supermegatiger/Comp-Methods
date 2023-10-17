from numpy import *
a,b,c = map(float,input().split())
L = 50
def solve(a,b,c):
    if a==b==c==0:
        print('бесконечно решений типа')
        return
    l,r = 1e-48,1e+48
    if (l < abs(a) < r) and (l < abs(b) < r) and (l < abs(c) < r):
        x1 = -(b+sign(b)*sqrt(b*b-4*a*c))/(2*a)
        x2 = c/(a*x1)
        res = []
        if l < abs(x1) < r:
            res.append(x1)
        if l < abs(x2) < r:
            res.append(x2)
        print(*sorted(res,key=lambda x: abs(x)))

def solve1(a,b,c):
    d = b*b - 4*a*c
    print(*sorted([(-b-sqrt(d))/(2*a),(-b+sqrt(d))/(2*a)],key=lambda x: abs(x)))

solve(a,b,c)
solve1(a,b,c)
