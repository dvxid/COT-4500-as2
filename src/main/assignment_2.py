import numpy as np

# variable declaration
xval = np.array([3.6,3.8,3.9])
yval = np.array([1.675, 1.436, 1.318])
x = 3.7

# formula from ch 3.1/3.2 slides
y = yval[0] * (((x - xval[1]) * (x-xval[2])) / ((xval[0]-xval[1]) * xval[0]-xval[2])) + yval[1] * (((x - xval[0]) * (x-xval[2])) / ((xval[1]-xval[0]) * xval[1]-xval[2])) + yval[2] * (((x - xval[0]) * (x-xval[1])) / ((xval[2]-xval[0]) * xval[2]-xval[1]))

print(y, '\n')


# Number 2
matrix = np.empty((4,5))

#storing given values in the matrix
# x values
matrix[0,0] = 7.2
matrix[1,0] = 7.4
matrix[2,0] = 7.5
matrix[3,0] = 7.6

# f(x) values
matrix[0,1] = 23.5492
matrix[1,1] = 25.3913
matrix[2,1] = 26.8224
matrix[3,1] = 27.4589

# first divided differences
matrix[1,2] = (matrix[1,1] - matrix[0,1]) / (matrix[1,0] - matrix[0,0]) 
matrix[2,2] = (matrix[2,1] - matrix[1,1]) / (matrix[2,0] - matrix[1,0])
matrix[3,2] = (matrix[3,1] - matrix[2,1]) / (matrix[3,0] - matrix[2,0])

# second divided differences
matrix[2,3] = (matrix[2,2] - matrix[1,2]) / (matrix[2,0] - matrix[0,0])
matrix[3,3] = (matrix[3,2] - matrix[2,2]) / (matrix[3,0] - matrix[1,0])

# third diveded differences
matrix[3,4] = (matrix[3,3] - matrix[2,3]) / (matrix[3,0] - matrix[0,0])

# calculating approximations for x = ?
P1 = matrix[0,1] + (x - matrix[0,0]) * matrix[1,2]
P2 = P1 + (x - matrix[0,0]) * (x - matrix[1,0]) * matrix[2,3]
P3 = P2 + (x - matrix[0,0]) * (x - matrix[1,0]) * (x - matrix[2,0]) * matrix[3,4]

print (P1)
print (P2)
print (P3, '\n')




