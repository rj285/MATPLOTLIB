import matplotlib.pyplot as plt
import numpy as np 

fig,axs = plt.subplots(4,2, figsize=(20,20))

x1 = np.array([0,6])
y1 = np.array([0,250])
axs[0,0].plot(x1,y1)
axs[0,0].set_title('PLOT 1')

x2 = np.array([1,8])
y2 = np.array([3,10])
axs[0,1].plot(x2,y2)
axs[0,1].set_title('PLOT 2')

x3 = np.array([1,8,3,10,5,7])
axs[1,0].plot(x3)
axs[1,0].set_title('PLOT 3')

x4 = np.array([1,2,6,8])
y4 = np.array([3,8,1,10])
axs[1,1].plot(x4,y4)
axs[1,1].set_title('PLOT 4')

ypoints = np.array([3, 8, 1, 10, 5, 7])
axs[2, 0].plot(ypoints)
axs[2, 0].set_title("PLOT 5")

ypoints = np.array([3, 8, 1, 10])
axs[2, 1].plot(ypoints, marker='o')
axs[2, 1].set_title("PLOT 6")

axs[3, 0].plot(ypoints, linestyle='dotted')
axs[3, 0].set_title("PLOT 7")

axs[3, 1].plot(ypoints, linestyle='dashed')
axs[3, 1].set_title("PLOT 8")

# Set the overall title for the figure
fig.suptitle("Multiple Plots")

# Adjust the spacing between subplots
plt.tight_layout()

plt.savefig('all_subplot.png')