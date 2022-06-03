

# numpy exercises

This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow
and in the numpy documentation. The goal of this collection is to offer a quick reference for both old
and new users but also to provide a set of exercises for those who teach.


If you find an error or think you've a better way to solve some of them, feel
free to open an issue at <https://github.com/rougier/numpy-100>.
File automatically generated. See the documentation to update questions/answers/hints programmatically.

#### 1. Import the numpy package under the name `np` (★☆☆)
import numpy as np

#### 2. Create a null vector of size 10 (★☆☆)
null_ten = np.zeros(10)

#### 3. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
null_ten_fifth_one = np.zeros(10)
null_ten_fifth_one[4] = 1

#### 4. Create a vector with values ranging from 10 to 49 (★☆☆)
null_ten_10_49 = np.arange(10, 50)

#### 5. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
zero_8 = np.arange(0, 9).reshape(3, 3)

#### 6. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
np_array_example = np.nonzero([1, 2, 0, 0, 4, 0])

#### 7. Create a 3x3 identity matrix (★☆☆)
identity_matrix = np.eye(3)

#### 8. Create a 3x3x3 array with random values (★☆☆)
random_3_to_3 = np.random.random((3, 3, 3))

#### 9. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
x = np.random.random((5,5))
xmin, xmax = x.min(), x.max()
print(xmin, xmax)

#### 10. Create a random vector of size 30 and find the mean value (★☆☆)
mean_reandom_30 = np.random.random(10).mean()

#### 11. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
np.diag([1, 2, 3, 4, 5])

#### 12. Normalize a 5x5 random matrix (★☆☆)
`hint: (x -mean)/std`
x = np.random.random((5, 5))
(x - x.mean()) / x.std()

#### 13. How to find common values between two arrays? (★☆☆)
`hint: np.intersect1d`
ar1 = np.array([0, 1, 2, 3, 4])
ar2 = [1, 3, 4]
print(np.intersect1d(ar1, ar2))

#### 14. Create a random vector of size 10 and sort it (★★☆)
`hint: sort`
x = np.random.random(11)
print(np.sort(x))

#### 15. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
`hint: argmax`
x = np.random.random(11)

x = np.sort(x)

x[-1] = 10

print(x)

#### 16. Subtract the mean of each row of a matrix (★★☆)
`hint: mean(axis=,keepdims=)`
a = np.random.rand(3, 4)

b = a - a.mean(axis=1, keepdims=True)

#### 17. How to get the n largest values of an array (★★★)
arr = np.array([2, 0, 1, 5, 4, 1, 9])

sorted_array = arr[np.argsort(arr)]

n=1

result = sorted_array[-n:][0]

#### 18. Create a random 5*3 matrix and replace items that are larger than 4 by their squares ( Example:  6 --> 36) 
`hint: np.where`

data = np.random.randint(-10, 10, size=(5, 3))

data = np.where(data > 4, data ** 2, data)

print(data)
