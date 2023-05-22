import numpy as np

arr = np.arange(100000000)
np.random.shuffle(arr)
np.savetxt("./unsorted_file.txt", arr, fmt = '%d')