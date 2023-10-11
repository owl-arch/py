##
# Referências:
#   https://www.w3schools.com/python/
#   https://www.w3schools.com/python/numpy/default.asp
##


from scipy import stats

import numpy as np
print(' Importing NumPy and checkingits version:\n', np.__version__)
print()

##
# Array Creation
##

# From a list
arr = np.array([1, 2, 3, 4, 5])
print(' From a list:\n', arr)
print()

# Array of zeros
arr = np.zeros((3, 3))
print(' Array of zeros:\n', arr)
print()

# Array of ones
arr = np.ones((3, 3))
print(' Array of ones:\n', arr)
print()

# Array with a range of values
arr = np.arange(0, 10)
print(' Array with a range of values:\n', arr)
print()

# Array of random values
arr = np.random.rand(3, 3)
print(' Array of random values:\n', arr)
print()

##
# Array Attributes
##

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(' Array Attributes:\n', arr)
print()

# Shape
print(' Shape:\n', arr.shape)
print()

# Data type
print(' Data type:\n', arr.dtype)
print()

##
# Indexing and Slicing
##

# Indexing and Slicing
arr = np.array(([1, 2, 3, 4, 5]))
print(' Indexing and Slicing:\n', 'arr = ', arr)
print()

# Get the first element
print(' Get the first element:\n', arr[0])
print()

# Get the last element
print(' Get the first element:\n', arr[-1])
print()

# Get slice from the second to the fourth element
print(' Get slice from the second to the fourth element:\n', arr[1:4])
print()

##
# Array Manipulation
##

#  Array Manipulation
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(' Array Attributes:\n', arr)
print()

# Reshape
arr_reshaped = arr.reshape((3, 2))
print(' Reshape:\n', arr_reshaped)
print()

# Vertical stack
arr_stack = np.vstack([arr, arr])
print(' Vertical stack:\n', arr_stack)
print()

##
# Arithmetic Operations
##

#  Arithmetic Operations
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(' Array Attributes:\n')
print(' arr1 = ', arr1)
print(' arr2 = ', arr2)
print()

# Addition print
print(' Addition:', (arr1 + arr2))

# Substraction print
print(' Substraction:', (arr1 + arr2))

# Multiplication print
print(' Multiplication:', (arr1 * arr2))

# Division print
print(' Division:', (arr1 / arr2))
print()

##
# Statistical Operations
# https://byjus.com/statistics-formulas/
##

#  Array Manipulation
arr = np.array([0, 1, 2, 3, 4, 2, 5, 3, 3])
print(' Array Attributes:', arr)
print()

# Mean (Significado)
# Média = soma(x)/n
print(' Mean:', np.mean(arr))
print()

# Median (Mediana)
print(' Median:', np.median(arr))
print()

# Mode (moda)
# find unique values in array along with their counts
# encontre valores únicos no array junto com suas contagens
values, counts = np.unique(arr, return_counts=True)
# find mode (encontrar moda)
mode_value = np.argwhere(counts == np.max(counts))
print(' Mode:', mode_value)
print(' Mode:', stats.mode(arr))
print()

# Variance (variancia)
print(' Variance:', np.var(arr))
print()

# Standard Deviation (desvio padrão)
print(' Standard Deviation:', np.std(arr))
print()
