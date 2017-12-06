import numpy as np
import matplotlib.pyplot as plt


xdata = np.linspace(-5.0,5.0,1024)
ydata = np.exp(-xdata**2.0)
plt.style.use("custom_plot_style.py")
plt.figure("After using style")
plt.plot(xdata,ydata)
plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()
