import matplotlib.pyplot as plt
import numpy as np

x = [0.74, 0.7597444, 0.6354, 1.15, 0.7589, .936, .97]
y = [0.27337661385536194, 0.3012211322784424, 0.3469989661127329, 0.2703763902187347, 0.3279898762702942, 0.5625500679016113, 0.3827874958515167]

m = [1.9173, 1.718, 1.862, 1.96, 1.435, 1.8, 1.53]
n = [0.3137609541416168, 0.16973263770341873, 0.2172022618353367, 0.20757025914887586, 0.32909549623727796, 0.3531190514564514, -0.07495249062776566]

x_ax = np.linspace(0.5,2,100)
y_ax = 0.5*x_ax-0.25
plt.plot(x_ax, y_ax, '-r')

#plt.scatter(x, y, c="blue")
#plt.scatter(m,n, c="green")

labels1 = [' CS 59SI -> APPHYS 282', ' CS 129 -> CS 230', ' ENGR 108 -> MATH 104', ' CS 154 -> POLISCI 1', ' ECON 113 -> ECON 131', ' PSYCH 288 -> PSCYH 137', ' CS 106B -> CS 166']
labels2 = [' CS 59SI -> CS 83', ' CS 129 -> CS 131', ' ENGR 108 -> ENGR 110', ' CS 154 -> CS 155', ' ECON 113 -> ECON 118', ' PSYCH 288 -> PSCYH 289', ' CS 106B -> CS 107']

for index, y_val in enumerate(y):
     x_val = x[index]
     label = labels1[index]
     plt.scatter(x_val, y_val, c="blue", label=label)
     plt.annotate(label, (x_val, y_val), fontsize=7.5)

for index, m_val in enumerate(m):
     n_val = n[index]
     label = labels2[index]
     plt.scatter(m_val, n_val, c="green", label=label)
     plt.annotate(label, (m_val, n_val), fontsize=7.5)

# Get the legend to proper location
# plt.legend(loc = "upper right")

# To show the plot
plt.show()