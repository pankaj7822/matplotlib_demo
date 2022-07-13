# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# define data values
y1 = np.array([20210.60,21008.50,21586.50,20290.40,20019.80,19894.70,19777.80,19433.80,19110.40,19086.20,19036.10,19022.50,19019.60]) # X-axis points
x1 = np.array([i+1 for i in range(len(y1))]) 

y2=np.array([20010.60,20860.90,20568.60,20280.50,20008.80,19666.80,19589.60,19285.60,19022.60,18922.70,18888.80,18813.40,18800.80,18755.80,18742.60])
x2 = np.array([i+1 for i in range(len(y2))])

plt.plot(x1, y1,label="Price GA (₹)",marker="o") # Plot the chart
plt.plot(x2, y2,label="Price PGA (₹)",marker="o") # Plot the chart
plt.legend()
plt.xlabel("Trials")
plt.ylabel("Price")
plt.savefig("plot3.jpeg")