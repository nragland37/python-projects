import matplotlib.pyplot as plt

# simple plot
plt.plot([1, 2, 3, 4])
plt.ylabel("some numbers")
plt.show()

# simple plot with x and y
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

# formatting the style of the plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
plt.axis([0, 6, 0, 20])  # [xmin, xmax, ymin, ymax]
plt.show()

# using numpy to generate plots
import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0.0, 5.0, 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
plt.show()
