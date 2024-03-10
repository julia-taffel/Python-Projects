import random
matrix1 = [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
]
matrix2 = [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
]
matrix_sum = [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
]
print ('Enter number of rows up to 5')
row = int(input())
print ('Enter number of columns up to 5')
column = int(input())
for i in range(row):
      for j in range(column):
            matrix1[i][j] = random.randint(1,100)
for i in range(row):
      for j in range(column):
            matrix2[i][j] = random.randint(1,100)
            matrix_sum[i][j] = matrix1[i][j] + matrix2[i][j]
print('Matrix 1')
for i in range(row):
      for j in range(column):
            print(matrix1[i][j], end=" ")
print('Matrix 2')
for i in range(row):
      for j in range(column):
            print(matrix2[i][j], end=" ")
print('Matrix sum')
for i in range(row):
      for j in range(column):
            print(matrix_sum[i][j], end =" ")
      print(' ')