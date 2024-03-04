import matplotlib.pyplot as plt
import numpy as np

fig,axs = plt.subplots(4,2, figsize=(20,20))

xpoints = np.array([0,6])
ypoints = np.array([0,250])
axs[0,0].plot(xpoints,ypoints)
axs[0,0].set_title('PLOT 1')

xpoint = np.array([1,8])
ypoint = np.array([3,10])
axs[0,1].plot(xpoint,ypoint)
axs[0,1].set_title('PLOT 2')

plt.savefig('subplot4.png')