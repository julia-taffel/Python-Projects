from time import time

def czas():
    before = time()
    while True:
        now = time()
        yield now - before
        before = now
    
for r in czas():
    print(r)
