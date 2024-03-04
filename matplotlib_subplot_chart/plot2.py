import matplotlib.pyplot as plt
import numpy as np

# x_points = np.array([0, 6])
# y_points = np.array([0, 250])

x_points = np.array([1, 2, 6, 8])
y_points = np.array([3, 8, 1, 10])

plt.plot(x_points, y_points)
plt.savefig('plot2.png')  # Save the plot as a PNG file
plt.show()
