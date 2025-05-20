from secrets import randbelow
from Crypto.Util.number import getPrime

p = getPrime(2048)
g = 2
print("Prime p: ", p)
print("Prime g: ", g)

#Alice
a = randbelow(p)
A = pow(g, a, p)
print("Alice private key: ", a)
print("Alice public value: ", A)

#Bob
b = randbelow(p)
B = pow(g, b, p)
print("Bob private key: ", b)
print("Bob public value: ", B)

#Shared secret
S_alice = pow(B, a, p)
S_bob = pow(A, b, p)
print("Alice shared secret key: ", S_alice)
print("Bob shared secret key: ", S_bob)

assert S_alice == S_bob
