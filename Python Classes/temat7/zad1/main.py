from functools import partial

def grawitacja(m1, m2, r):
    return G * m1 * m2 / r**2

G = 6.674 * 10**-11
MASA_ZIEMI = 5.972 * 10**24
PROMIEN_ZIEMI = 6.371 * 10**6

#def grawitacja_ziemi(MASA_ZIEMI, PROMIEN_ZIEMI):
#    def f(m2):
#        return grawitacja(MASA_ZIEMI, m2, PROMIEN_ZIEMI)
#    return f(1)
#def grawitacja_ziemi(MASA_ZIEMI, PROMIEN_ZIEMI):
#    return partial(grawitacja, MASA_ZIEMI, r=PROMIEN_ZIEMI)

def closure(m, p):
    def f(x):
        return grawitacja(m, x, p)
    return f

grawitacja_ziemi = closure(MASA_ZIEMI, PROMIEN_ZIEMI)

print(grawitacja_ziemi(2))
