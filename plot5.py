# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# define data values
points1=[(1,5622), (2,12220), (3,19808), (4,25893), (5,32346)]
y1 = np.array([ele[1] for ele in points1]) # X-axis points
x1 = np.array([str(i+1) for i in range(len(y1))]) 

points2=[(1, 5410), (2, 12080), (3,19286), (4,25104), (5,32126)]
y2=np.array([ele[1] for ele in points2])
x2 = np.array([str(i+1) for i in range(len(y2))])

plt.plot(x1, y1,label="Price GA (₹)",marker="o") # Plot the chart
plt.plot(x2, y2,label="Price PGA (₹)",marker="o") # Plot the chart
plt.legend()
plt.title("36 Nodes System")
plt.xlabel("Number Of vehicles")
plt.ylabel("Price")
plt.savefig("plot5.jpeg")