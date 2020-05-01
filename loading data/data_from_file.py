import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('example1.txt', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x.append(int(row[0]))
        y.append(int(row[1]))

print(x)
print(y)

plt.plot(x, y, label='Loaded from file (csv)')

plt.xlabel('x')
plt.ylabel('y')

plt.title('Loading Data from a CSV file')
plt.legend()
plt.show()
