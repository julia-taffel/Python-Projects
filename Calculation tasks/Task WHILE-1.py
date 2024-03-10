import random
num = []
num.append(0)
i=1
#print('Enter', 1, 'number')
num[0] = random.randint(1,4)
print ('[ 1 ]', num[0])
num_sum=num[0]
num_min=num[0]
num_max=num[0]
while i < 10 :
    #print('Enter', i+1, 'number')
    num.append(0)
    num[i] = random.randint(1, 4)
    print ('[',i+1,']', num[i])
    num_sum = num_sum + num[i]
    if num[i] < num_min:
      num_min = num[i]
    if num[i] > num_max:
      num_max = num[i]
    if num_max == num_min *4 :
      break
    i += 1
print("The sum of entered number is", num_sum)
print('min =', num_min)
print('max =', num_max)