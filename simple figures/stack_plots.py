import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

sleeping =[5,6,7,8,5,6,9]
eating =[2,3,4,3,2,1,2]
working =[8,8,8,9,10,12,2]
playing =[1,2,3,1,2,5,3]

plt.stackplot(days,sleeping, eating, working, playing, colors = ['blue','yellow','pink','green'])

plt.xlabel('x axis')
plt.ylabel('y axis')

plt.legend()
plt.title('Histogram')

plt.show()