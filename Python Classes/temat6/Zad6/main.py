def multiply(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            yield f"{i}x{j}={i * j}"

n=int(input())

#wyjscie = multiply(n)

wyjscie = [f"{i}x{j}={i * j}" for i in range(1, n+1) for j in range(1, n+1)]

for line in wyjscie:
    print(line)