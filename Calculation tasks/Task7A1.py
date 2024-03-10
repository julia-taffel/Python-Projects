n = int(input('Enter n:'))
print('Enter', 1, 'number')
num = float(input())
while num <=0:  
    print('Enter', 1, 'number')
    num = float(input())
num_sum=num
num_min=num
num_max=num
i=1
while i < n:
    print('Enter', i+1, 'number')
    prev = num
    num = float(input())
    if num <= 0:
       continue
    num_sum = num_sum + num
    if num < num_min:
      num_min = num
    if num > num_max:
      num_max = num
    i += 1
x = num_sum/n
print("The average of entered numbers is", x)
print("The sum of entered number is", num_sum)
print('min =', num_min)
print('max =', num_max)