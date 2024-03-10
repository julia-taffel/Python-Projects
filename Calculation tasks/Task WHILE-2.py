import random
print ('Enter how many numbers')
n = int (input ())
num = []
num.append(0)
i=1
while num[0] <=0:  
    #print('Enter', 1, 'number')
    num[0] = random.randint(-100,100)
print ('[ 1 ]', num[0])
num_sum=num[0]
num_min=num[0]
num_max=num[0]
while i < n:
    #print('Enter', i+1, 'number')
    num.append(0)
    num[i] = random.randint(-100, 100)
    if num[i] <= 0:
       continue
    print ('[',i+1,']', num[i])
    num_sum = num_sum + num[i]
    if num[i] < num_min:
      num_min = num[i]
    if num[i] > num_max:
      num_max = num[i]
    i += 1
x = num_sum/n
print("The average of entered numbers is", x)
print("The sum of entered number is", num_sum)
print('min =', num_min)
print('max =', num_max)