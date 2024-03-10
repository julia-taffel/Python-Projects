import random
#print ('Enter how many numbers')
#n = int (input ())
num = []
num.append(0)
num[0] = random.randint(1, 100)
print ('[ 1 ]', num[0])
num_sum = num[0]
mini = num[0]
maxi = num[0]
i=1
num.append(0)
num[i] = random.randint(1, 100)
print ('[',i+1,']', num[i])
num_sum = num_sum + num[i]
if num[i] < mini:
  mini = num[i]
if num[i] > maxi:
  maxi = num[i]
while num[i] != num[i-1] :
   i=i+1
   num.append(0)
   num[i] = random.randint(1, 100)
   print ('[',i+1,']', num[i])
   num_sum = num_sum + num[i]
   if num[i] < mini:
      mini = num[i]
   if num[i] > maxi:
      maxi = num[i]
print ('sum =', num_sum)
print ('max =', maxi)
print ('min =', mini)