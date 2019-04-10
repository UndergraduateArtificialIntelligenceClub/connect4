import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# now we put machine learning stuff here


# plotting the learning
x = np.linspace(-100, 100, 50)
y = x**2
plt.plot(x, y)
plt.savefig('plot.png')