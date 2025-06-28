import numpy as np
arr = np.array([10, 40, 5, 100])
print("Max value:", arr.max())

print("Min value:", arr.min())

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
rows, cols = arr2d.shape
print("Rows:", rows, "Cols:", cols)

print("Element at [1,2]:", arr2d[1, 2])

print("All elements:")
for i in arr2d.flatten():
    print(i, end=' ')

sum_val = 0
for row in arr2d:
    for item in row:
        sum_val += item
print("\nSum using loop:", sum_val)



x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

print("Addition:\n", x + y)
print("Subtraction:\n", x - y)
print("Multiplication:\n", x * y)
print("Division:\n", x / y)
