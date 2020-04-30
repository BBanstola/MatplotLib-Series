import matplotlib.pyplot as plt

population_ages = [2,4,8,12,15,5,10,16,13,19,12,24,18,3,5,25,20,6,1,5,56,74,85,23,54,95,62,12,45,65,25,85]

#ids = [x for x in range(len(population_ages))]

#plt.bar(ids, population_ages)

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(population_ages,bins, histtype='bar', rwidth=0.5)

plt.xlabel('x axis')
plt.ylabel('y axis')


plt.title('Histogram')

plt.show()