from matplotlib import pyplot as plt
import numpy as np
import math #needed for definition of pi
x = np.arange(0, math.pi*2, 0.05)
y = np.tan(x)
plt.plot(x,y)
plt.xlabel("Date")
plt.ylabel("Ratio")
plt.title('COVID ratio of deaths to actual deaths')
plt.show()