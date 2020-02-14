import re
import matplotlib.pyplot as plt

# plot the training loss func

f = open('log.txt', 'r')
res = []
x_axis = []
y_axis = []
for line in f:
    if re.search('loss', line):
        res.append(line.split()[6:10])
print(float(res[0][3]))
for line in range(len(res)):
    x_axis.append(float(res[line][1]))
    y_axis.append(float(res[line][3]))

print(x_axis)
print(len(x_axis))
print(y_axis)
print(len(y_axis))

plt.plot(x_axis, y_axis)
plt.show()
