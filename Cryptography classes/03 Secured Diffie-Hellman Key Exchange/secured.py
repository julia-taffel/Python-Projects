from secrets import randbelow
from Crypto.Util.number import getPrime
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

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

alice_rsa = RSA.generate(2048)
bob_rsa = RSA.generate(2048)

hash_A = SHA256.new(str(A).encode())
signature_A = pkcs1_15.new(alice_rsa).sign(hash_A)

hash_B = SHA256.new(str(B).encode())
signature_B = pkcs1_15.new(bob_rsa).sign(hash_B)

pkcs1_15.new(bob_rsa.publickey()).verify(hash_B, signature_B)
pkcs1_15.new(alice_rsa.publickey()).verify(hash_A, signature_A)

S_alice = pow(B, a, p)
S_bob = pow(A, b, p)

assert S_alice == S_bob