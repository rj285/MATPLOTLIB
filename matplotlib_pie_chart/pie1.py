import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabel = ["Apples","Banana","Cherries","Dates"]
plt.pie(y, labels= mylabel, startangle=90)
plt.show()

plt.savefig('PIE 1')