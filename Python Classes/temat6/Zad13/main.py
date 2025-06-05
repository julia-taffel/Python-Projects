import math

def pole_trojkata(a = None, b = None, c = None, ha = None, hb = None, hc = None, alfa = None, beta = None, gamma = None):
	if a and ha:
		return 0.5*a*ha
	if b and hb:
		return 0.5*b*hb
	if c and hc:
		return 0.5*c*hc
	if a and b and gamma:
		return 0.5*a*b*math.sin(gamma)
	if a and c and beta:
		return 0.5*a*c*math.sin(beta)
	if b and c and alfa:
		return 0.5*b*c*math.sin(alfa)
	if a and b and c:
		p = (a+b+c)/2
		return math.sqrt(p(p-a)(p-b)*(p-c))
	return 0

wejscie = [
    {'a': 5, 'ha': 3},
    {'a': 3, 'b': 4, 'c': 5},
    {'a': 6, 'b': 8, 'gamma': 1.0472},
    ]

for r in wejscie:
    print(pole_trojkata(**r))