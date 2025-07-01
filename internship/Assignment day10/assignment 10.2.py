import numpy as np

array3d = np.arange(2*3*4).reshape(2,3,4)

moved = np.moveaxis(array3d, 0, -1)
print("Moved axes:\n", moved)
