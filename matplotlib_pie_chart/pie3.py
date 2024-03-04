import matplotlib.pyplot as plt
import numpy as np

z = np.array([35,25,25,15])
datas = ["Apple","Banana","Orange","Grapes"]
cls = ["red","yellow","orange","magenta"]
plt.pie(z, labels=datas, startangle=90, colors=cls)
plt.legend(title = "FRUITS")
plt.show()

plt.savefig('PIE 3')