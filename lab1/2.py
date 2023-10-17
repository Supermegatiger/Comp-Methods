from numpy import *


accuracy = 0.5e-8
x_answers = [pi*pi/6, 1.53460724490456065438295871072, 1.44087884154672282529652063816,1.36008258678244401658450305348, 1.28957780079104178718959152009,1.22741127776021876233107151417,1.17210519612501518752085801324,1.12251934253575259612353753442,1.07775887274424300151901807116,1.03711091785065842203471019335,1]

# вычисление ϕ(x)

# for x in zip(arange(0,1.1,0.1),x_answers):
#     k = 1
#     tek = 1/(k*k + k*x[0])
#     res = tek
#     while abs(res-x[1]) > accuracy:
#         # if k%10000000 == 0:
#         #     print(res, abs(res-x[1]) - accuracy)
#         k+=1
#         tek = 1/(k*k + k*x[0])
#         if(res + tek == res):
#             break
#         res += tek
#     print(f'x = {x[0]:.1f}; k = {k}; f = {res}')

# вывод:

# x = 0.0; k = 94906266; f = 1.644934057834575
# x = 0.1; k = 94906266; f = 1.534607235890896
# x = 0.2; k = 94906266; f = 1.4408788325330346
# x = 0.3; k = 94906266; f = 1.3600825777688073
# x = 0.4; k = 94906266; f = 1.2895777917774045
# x = 0.5; k = 94906266; f = 1.227411268746524
# x = 0.6; k = 94906266; f = 1.1721051871113162
# x = 0.7; k = 94906266; f = 1.1225193335220283
# x = 0.8; k = 94906266; f = 1.0777588637305004
# x = 0.9; k = 94906266; f = 1.0371109088369574
# x = 1.0; k = 134217728; f = 0.9999999936264042

# вычисление ϕ(x) − ϕ(1)

for x in zip(arange(0,1.1,0.1),x_answers):
    k = 1
    tek = 1/(k*k + k*x[0]) - 1/k + 1/(k+1)
    res = tek
    while abs(res+1-x[1]) > accuracy:
        # if k%10000000 == 0:
        #     print(res, abs(res+1-x[1]) - accuracy)
        k+=1
        tek = 1/(k*k + k*x[0]) - 1/k + 1/(k+1)
        if(res + tek == res):
            break
        res += tek
    print(f'x = {x[0]:.1f}; k = {k}; f = {res+1}')

# вывод (+1):

# x = 0.0; k = 10000; f = 1.644934061849058
# x = 0.1; k = 9486; f = 1.534607239904593
# x = 0.2; k = 8944; f = 1.4408788365474252
# x = 0.3; k = 8366; f = 1.3600825817828412
# x = 0.4; k = 7745; f = 1.2895777957910444
# x = 0.5; k = 7071; f = 1.2274112727615374
# x = 0.6; k = 6324; f = 1.1721051911257705
# x = 0.7; k = 5477; f = 1.1225193375372877
# x = 0.8; k = 4472; f = 1.0777588677463983
# x = 0.9; k = 3162; f = 1.037110912853363
# x = 1.0; k = 1; f = 1.0

# как можно заметить, разность ϕ(x) − ϕ(1) действительно сходится быстрее