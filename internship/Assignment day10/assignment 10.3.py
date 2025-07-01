import numpy as np

arr = np.array([[6, np.nan, 73],
                [4, 12, np.nan]])

col_mean = np.nanmean(arr, axis=0)

inds = np.where(np.isnan(arr))
arr[inds] = np.take(col_mean, inds[1])
print("NaN replaced with column mean:\n", arr)
