import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100) 
y = np.sin(x) 


plt.plot(x, y, label='Sine Wave')


plt.title('Sine Wave Plot')
plt.xlabel('X values')
plt.ylabel('Y = sin(X)')


plt.legend()
plt.show()
