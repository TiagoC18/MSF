import matplotlib.pyplot as plt
import numpy as np

T = np.arange(0, 10, 1)
D = np.array([0.00, 0.735, 1.1363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])

aprox = np.polyfit(T, D, 1)

print("m = ", aprox[0])
print("b = ", aprox[1])