import matplotlib.pyplot as plt
import numpy as np


with open("settings.txt", 'r') as settings:
    tmp = [float(i[:-1]) for i in settings.readlines()]

dV = tmp[1]
T = tmp[0]

# collecting data from data file
data_array = np.loadtxt("data.txt", dtype=int)
data_array = data_array*dV

n = len(data_array)
times = np.linspace(0, T*(n-1), n)

fig, ax = plt.subplots(figsize=(16, 9))
ax.plot(times, data_array, color='red', label='V(t)', linestyle='-', marker='*')
ax.legend()

# set lims
min_v = data_array.min()
max_v = data_array.max()
max_t = T*n
res = ((np.where(data_array==max_v)[0][0])+1)*T
ax.set_ylim(min_v, 3.3)
ax.set_xlim(0, max_t)

# micro markers and grid
plt.minorticks_on()
plt.grid(which='major')
plt.grid(which='minor', linestyle=':')

# x, y and graph title
ax.set_title("Зарядка кондесатора", wrap=True)
ax.set_ylabel("Напряжение, B")
ax.set_xlabel("Время, c")

# placing text
y1 = max_v/2
x1 = max_t*0.75

y2 = y1-0.08
x2 = max_t*0.75

ax.text(x1, y1, f'Время зарядки = {round(max_t-res, 3)} c')
ax.text(x2, y2, f'Время разрядки = {round(res, 3)} c')

plt.savefig('graph')
plt.show()