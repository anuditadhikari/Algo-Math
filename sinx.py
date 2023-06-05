# import numpy
# import matplotlib.pyplot as plot

# x=numpy.arrange(0,10,0.1)
# sinx=numpy.sin(x)
# plot.plot(x,sin(x))
# h=0.00001
# fdx=(numpy.sin(x+h)-numpy.sin(x))/h
# plot.plot(x,fdx)
# plot.show()
import numpy as np
import matplotlib.pyplot as plt


# Define the function and its derivative
def f(x):
    return np.sin(x)


def f_prime(x):
    return np.cos(x)


# Generate x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

# Calculate y values
y = f(x)
y_prime = f_prime(x)

# Plot the function and its derivative
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="sin(x)")
plt.plot(x, y_prime, label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of sin(x) and its derivative")
plt.legend()
plt.grid(True)
plt.show()
