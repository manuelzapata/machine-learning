import matplotlib.pyplot as plt
import numpy as np

sleep = [5,6,7,8,10,12,16]
scores = [65,51,75,75,86,80,0]

coeffs = np.polyfit(sleep, scores, 2)
polynomial = np.poly1d(coeffs)

plt.scatter(sleep, scores)
x = range(0,17)
plt.plot(x, polynomial(x), color = "blue")
plt.xlabel("Sleep")
plt.ylabel("Scores")
plt.show()