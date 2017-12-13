import numpy as np
import matplotlib.pyplot as plt

x_ = np.arange(-3*2*np.pi, 3*2*np.pi, 0.05)
x = np.extract(np.abs(x_)>0.001,x_)
y = np.sin(x)/x
plt.plot(x,y)
plt.title('$\sin(x)/x $ v. $x$')
plt.show()

