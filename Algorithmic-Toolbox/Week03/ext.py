import numpy as np

a = np.array([1, 2, 3, 4])

a = np.pad(a, (0,), mode="constant")

print(a)