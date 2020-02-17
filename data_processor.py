import re
import matplotlib.pyplot as plt

# plot the training loss func

f = open('log.txt', 'r')
res = []
x_axis = []
y_axis = []
for line in f:
    if re.search('loss', line):
        # print(line.split())
        idx_iter = line.split().index('iter:')
        # print(idx_iter)
        res.append(line.split()[idx_iter:idx_iter+4])
# print(res)



for line in range(len(res)):
    x_axis.append(float(res[line][1]))
    y_axis.append(float(res[line][3]))

# print(x_axis)
# print(len(x_axis))
# print(y_axis)
# print(len(y_axis))

plt.plot(x_axis, y_axis)
plt.show()
