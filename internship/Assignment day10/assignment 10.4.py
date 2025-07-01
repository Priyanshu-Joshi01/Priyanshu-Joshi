import numpy as np

arr = np.array([[6, -8, 73, -110]])
arr[arr < 0] = 0
print("Negative values replaced with 0:\n", arr)
