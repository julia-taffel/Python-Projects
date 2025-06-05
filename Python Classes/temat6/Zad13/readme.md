Zadanie 13

Dana jest funkcja pole_trojkata, która oblicza pole trójkąta na podstawie: długości boków (a,b,c), wysokości (ha,hb,hc), miar kątów (alfa,beta,gamma), zależnie od przekazanych argumentów. Pod zmienną wejscie dostępna jest lista słowników, gdzie każdy słownik zawiera część z podanych wielkości. Dla każdego z podanych słowników, wypisz w oddzielnej linii jego pole, obliczając je przy pomocy funkcji pole_trojkata i korzystając z rozpakowywania.

Przykładowa implementacja funkcji (nie dołączaj jej do kodu)

def pole_trojkata(a = None, b = None, c = None, ha = None, hb = None, hc = None, alfa = None, beta = None, gamma = None):
	import math
	if a and ha:
		return 0.5aha
	if b and hb:
		return 0.5bhb
	if c and hc:
		return 0.5chc
	if a and b and gamma:
		return 0.5ab*math.sin(gamma)
	if a and c and beta:
		return 0.5ac*math.sin(beta)
	if b and c and alfa:
		return 0.5bc*math.sin(alfa)
	if a and b and c:
		p = (a+b+c)/2
		return math.sqrt(p(p-a)(p-b)*(p-c))
	return 0