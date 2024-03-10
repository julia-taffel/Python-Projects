import random
num = []
num.append(0)
num[0] = random.randint(1,100)
num_min = num[0]
num_max = num[0]
i=1
while i <10 :
  num.append(0)
  num[i] = random.randint(1,100)
  if num[i] < num_min :
    num_min = num[i]
  if num[i] > num_max :
    num_max = num[i]
  i=i+1
print('Max is', num_max)
print('Min is', num_min)
def calculations_from_numbers(x, y):
      return (x+y)/2
print('The average is', calculations_from_numbers(num_min, num_max))
