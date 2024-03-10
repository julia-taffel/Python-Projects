print('Task 2.1')
n = int(input('Enter n: '))
print('Enter 1 number')
num = float(input())
num_min = num
num_sum = num
num_max = num
for i in range (2, n+1):
  print('Enter ', i, ' number')
  num = float(input())
  if num < num_min :
    num_min = num
  if num > num_max :
    num_max = num
  num_sum = num_sum + num
x = num_sum/i
print('The sum of entered numbers is ', num_sum)
print('min = ', num_min)
print('max =', num_max)
print('The average of entered numbers is', x)
