import matplotlib.pyplot as plt
import numpy as np

fig,axs = plt.subplots(4,2, figsize=(10,10))

xpoints = np.array([1,8])
ypoints = np.array([3,10])

axs[0,1].plot(xpoints,ypoints)
axs[0,1].set_title("PLOT 2")

plt.savefig('subplot3.png')