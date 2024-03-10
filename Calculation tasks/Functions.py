def text_argument_function(text):
      return text

print(text_argument_function('Test text'))
def calculations_from_numbers(x, y, z):
      return x*(y + z)
print(calculations_from_numbers(2, 5, 7))
print(calculations_from_numbers(4, 1, 12))

#silnia
print("Enter n for calculate factorial: ",end="")
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
print ("The factorial of ", n ,"is: ",end="")
print (fact)

def fact(n):
  f = 1
  for i in range(1,n+1):
    f = f * i
  return f
print("Enter n for calculate factorial: ",end="")
n = int(input())
print ("The factorial of", n, " is: ",end="")
print (fact(n))