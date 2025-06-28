import numpy as np
a = np.array([7, 8, 9])
b = np.array([[1, 2, 3], [4, 5, 6]])

combined = np.append(b, [a], axis=0)

print("Combined array :\n", combined)
