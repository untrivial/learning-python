import numpy as np
a = np.array([1,2,3])
# np arrays work element-wise
# np arrays are 100-200x faster than lists in terms of math operations

a[0] = 5
print(a, a[0])
print(a.shape) # (3,)
print(a.dtype) # int64
print(a.ndim) # num of dimensions
print(a.size) # length of array
print(a.itemsize) # 8 bytes
a[0] = 1

b = a * np.array([1,2,3]) # 1,2,3 * 1,2,3 => 1,4,9
print(b)

a = a + np.array([4,4,4]) # 1,2,3 + 4,4,4 => 5,6,7
a = a + np.array([4]) # same as above, but broadcasting, now 9,10,11
a = a * 2 # 18,20,22

# 3 ways for dot product
a = np.array([1,2,3])
b = np.array([4,5,6])
dot = np.dot(a,b)
print(dot)

dot = (a * b).sum() # adds elements in array (can use np.sum)
print(dot)

dot = a @ b # same as above
print(dot)


# multidimensional arrays
# row, column
# flatten means putting into 1D array
a = np.array([[1,2,6], [3,4,8]])
print(a.shape) # (3,3)
print(a[0,0]) # same as a[0][0]

# slicing
print(a[:,0]) # [1, 3]
print(a[0,:]) # [1, 2, 6]
print(a[0,1:3]) # [2, 6]
print(a[-1,-1]) # starts from last index, 8

# transpose
print(a.T) # [1 3] [2 4] [6 8]

# linear algebra
a = np.array([[1,2], [3,4]])
print(np.linalg.inv(a)) # inverse
print(np.linalg.det(a)) # determinant

print(np.diag(a)) # diagonal elements
c = np.diag(a)
print(np.diag(c)) # matrix with only diagonal elements

# boolean indexing
a = np.array([[1,2], [3,4], [5,6]])
bool_idx = a > 2
print(bool_idx) # returns a matrix of booleans that satisfy condition
print(a[a > 2]) # returns 1D array (here 3,4,5,6)
b = np.where(a>2, a, -1) # to maintain same size
print(b)

# fancy indexing
# put indices that satisfy into an array, then index the original array with it
a = np.array([10,19,30,41,50,61])
print(a)
b = [1,3,5]
print(a[b]) # 19, 41, 61

a = np.array([10,19,30,41,50,61])
print(a)
even = np.argwhere(a % 2 == 0).flatten()
print(a[even]) # prints all the even numbers


# reshaping arrays
a = np.arange(1,7) # array from 1 to 6
b = a.reshape((2,3)) # two rows, three columns
c = a[np.newaxis, :] # puts array into a 1 by 6 2D array
c = a[:, np.newaxis] # puts array into a 6 by 1 2D array


# concatenation
a = np.array([[1,2], [3,4]])
b = np.array([[5,6]])
c = np.concatenate((a,b)) # adds b as a new row
c = np.concatenate((a,b), axis=None) # flattened into 1D array
c = np.concatenate((a,b.T), axis=1) # adds 5,6 as a column

# hstack
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.hstack((a,b)) # horizontal
print(c)

# vstack
c = np.vstack((a,b)) # adds b as a new row


# Broadcasting
# work with arrays of different shapes, don't need to match array dimensions perfectly
x = np.array([[1,2,3], [4,5,6], [1,2,3], [4,5,6]])
a = np.array([1,0,1])
y = x + a # adds 1, 0, 1 to each respective element ([2,2,4], etc)

# more functions
x = np.array([[1,2,3], [4,5,6], [1,2,3], [4,5,6]])
print(x.sum()) # sums all elements
    # axis=None is default
print(x.sum(axis=0)) # calculates column sums
print(x.sum(axis=1)) # calculates row sums

# data sciency functions
print(x.mean()) # find mean
print(np.mean(x, axis=None)) # same as above
print(x.var()) # variance
print(x.std()) # standard deviation
print(x.min())
print(x.max())

# data types
x = np.array([1.0,2.0], dtype=np.int64) # forced
    # also float64, int32, float32, int16, float16

# copying
b = a.copy() # shallow
    # no deepcopy()

# Zeroes and creating
a = np.zeros((2,3))
print(a) # array of 2 by 3 zeroes, float64
a = np.ones((2,3))
a = np.full((2,3), 5.0) # shape filled with 5.

a = np.eye(3)
# returns 3 by 3 matrix with diagonal ones and everything else zero

a = np.linspace(0,10,5) # start, stop, num of elements
    # elements are equally spaced


# Random Numbers
a = np.random.random((3,2)) # generates 3 by 2 with random numbers
a = np.random.randn(3,2) # does not take a tuple, normal/Gaussian
a = np.random.randint(3,10,size=(3,3)) # 3 by 3 matrix with random integers from 3 to 9
    # if you remove 3, it'll go from 0 to 10
a = np.random.choice(5, size=10) # 10 length array with random numbers from 0 to 5
a = np.random.choice([5,2,2], size=10) # chooses randomly from list


# eigenvalues and eigenvectors
a = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvalues)
print(eigenvectors) # column vector

# solving linear systems
A = np.array([[1, 1], [1.5, 4.0]])
b = np.array([2200, 5050])
x = np.linalg.solve(A, b)
print(x)


# loading data from CSV
# np.loadtxt, np.genfromtxt (preferred)
'''
data = np.loadtxt('spambase.csv', delimiter=',', dtype=np.float32)
print(data) # prints large array

data = np.genfromtxt('spambase.csv', delimiter=',', dtype=np.float32)
print(data)
'''