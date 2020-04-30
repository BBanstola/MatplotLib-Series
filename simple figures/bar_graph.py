import matplotlib.pyplot as plt

x = [2, 4, 8, 12, 15]
y = [5, 10, 16,13,19]

x2 = [12, 24, 18, 3, 5]
y2 = [25, 20, 6, 1, 5]


plt.bar(x, y, label='Bars  1', color='red')
plt.bar(x2,y2, label='bars 2', color='yellow')

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend()

plt.title(' Bar Graph')

plt.show()