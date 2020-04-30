import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10,11,12]
y = [10,20,30,40,50,12,13,15,16,45,21,32]

plt.scatter(x,y, label='skitskat', color='red', marker='*', s=15)

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend()
plt.title('Scatter Plotting')

plt.show()