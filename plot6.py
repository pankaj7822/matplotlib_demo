# importing the required libraries
import matplotlib.pyplot as plt
import numpy as np

# define data values
points1=[(1,5840), (2, 13466), (3, 21940), (4,27105), (5, 34343)]
y1 = np.array([ele[1] for ele in points1]) # X-axis points
x1 = np.array([str(i+1) for i in range(len(y1))]) 

points2=[(1, 5810), (2,13333), (3, 21440), (4, 27016), (5, 33926)]
y2=np.array([ele[1] for ele in points2])
x2 = np.array([str(i+1) for i in range(len(y2))])

plt.plot(x1, y1,label="Price GA (₹)",marker="o") # Plot the chart
plt.plot(x2, y2,label="Price PGA (₹)",marker="o") # Plot the chart
plt.legend()
plt.title("108 Nodes System")
plt.xlabel("Number Of vehicles")
plt.ylabel("Price")
plt.savefig("plot6.jpeg")