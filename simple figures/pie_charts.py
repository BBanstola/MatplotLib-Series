import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]


slices = [7,2,8,3]
act = ['eat','sleep','work','play']
colors = ['r','b','y','g']

plt.pie(slices,
        labels=act,
        colors= colors,
        startangle=0,
        shadow=True,
        autopct='%1.1f%%')

plt.title('Pie Chart')

plt.show()