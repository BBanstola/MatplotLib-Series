import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('example1.txt', delimiter=',', unpack=True)

plt.plot(x, y, label='Loaded from file (csv)')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Loading Data from a CSV file')
plt.legend()
plt.show()
