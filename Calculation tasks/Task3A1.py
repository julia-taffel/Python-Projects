print ('Enter how many numbers')
n = int (input ())
print ('Enter 1 number')
num = []
num.append(0)
num[0] = float (input ())
num_sum = num[0]
for i in range (1,n):
      num.append(0)
      print ('Enter',i+1, 'number')
      num[i] = float (input ())
      num_sum = num_sum + num [i]
x = num_sum/n
print ('Average is =', x)
count_min = 0
for i in range (n):
      if num[i] > x:
             count_min = count_min + 1
print ('Ilosc = ', count_min)