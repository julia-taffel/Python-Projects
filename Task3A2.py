
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
matrix3 = [
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
            print ('Enter element [',i+1,',',j+1,'] of matrix 1')
            matrix1[i][j] = float(input()) 
for i in range(row):
      for j in range(column):
            print ('Enter element [',i+1,',',j+1,'] of matrix 2')
            matrix2[i][j] = float(input())
for i in range(row):
      for j in range(column):
            print ('Enter element [',i+1,',',j+1,'] of matrix 3')
            matrix3[i][j] = float(input()) 
            matrix_sum[i][j] = matrix1[i][j] + matrix2[i][j] + matrix3[i][j]
print('Matrix sum')
for i in range(row):
      for j in range(column):
            print(matrix_sum[i][j]) 
print('Matrix sum')
for i in range(row):
      for j in range(column):
            print(matrix_sum[i][j], end =" ")
      print(' ') 