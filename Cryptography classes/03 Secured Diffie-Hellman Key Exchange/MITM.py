from secrets import randbelow
from Crypto.Util.number import getPrime

p = getPrime(2048)
g = 2

#Alice
a = randbelow(p)
A = pow(g, a, p)

#Bob
b = randbelow(p)
B = pow(g, b, p)

#Mallory
m1 = randbelow(p)
M1 = pow(g, m1, p)
m2 = randbelow(p)
M2 = pow(g, m2, p)

#Shared secret
S_alice = pow(M1, a, p)
S_bob = pow(M2, b, p)

S_mallory_A = pow(A, m2, p)
S_mallory_B = pow(B, m1, p)

assert S_alice == S_bob
assert S_alice == S_mallory_A
assert S_bob == S_mallory_B

#print("Alice shared secret key: ", S_alice)
#print("Bob shared secret key: ", S_bob)
