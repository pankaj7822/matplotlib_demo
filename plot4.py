# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# define data values
y1 = np.array([34882.50,35267.60,35788.80,34290.60,34186.70,34040.00,33916.20,33890.40,33850.60,33844.00,33820.00,]) # X-axis points
x1 = np.array([i+1 for i in range(len(y1))]) 

y2=np.array([34000.00,34816.60,34980.60,34530.00,34375.20,34010.40,33910.00,33833.80,33696.10,33602.20,33540.60,33506.80,33426.40,33376.60,33290.80])
x2 = np.array([i+1 for i in range(len(y2))])

plt.plot(x1, y1,label="Price GA (₹)",marker="o") # Plot the chart
plt.plot(x2, y2,label="Price PGA (₹)",marker="o") # Plot the chart
plt.legend()
plt.xlabel("Trials")
plt.ylabel("Price")
plt.savefig("plot4.jpeg")