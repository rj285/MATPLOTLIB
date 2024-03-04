import matplotlib.pyplot as plt
import numpy as np

x = np.array([35,25,25,15])
datas = ["Apple","Banana","Orange","Grapes"]
colors = ["Red","Yellow","Orange","Magenta"]
plt.pie(x,labels=datas, colors=colors, startangle=90)
plt.show()

plt.savefig('PIE 2')
