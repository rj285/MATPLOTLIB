import matplotlib.pyplot as plt
import numpy as np

fig,axs = plt.subplots(4,2, figsize=(10,10))

xpoints = np.array([0,6])
ypoints = np.array([0,250])
axs[0,0].plot(xpoints,ypoints)
axs[0,0].set_title("PLOT 1")

plt.savefig("subplot2.png")