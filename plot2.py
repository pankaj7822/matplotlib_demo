import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
 
# Dataset
case1_y=np.array([18,20, 28,30, 26, 24, 28])
case2_y=np.array([18,20, 25,35,26,22,28 ])
x=np.array([i+1 for i in range(len(case1_y))])

 
cubic_interploation_model_case1 = interp1d(x, case1_y, kind = "cubic")
cubic_interploation_model_case2 = interp1d(x, case2_y, kind = "cubic")

 
# Plotting the Graph
X_=np.linspace(x.min(), x.max(), 500)
case_1_Y_=cubic_interploation_model_case1(X_)
case_2_Y_=cubic_interploation_model_case2(X_)
 
plt.plot(X_, case_1_Y_,label="Case 1")
plt.plot(X_, case_2_Y_,label="Case 2")
plt.legend()
plt.xlabel("Number Of Iteration")
plt.ylabel("Cost")
plt.savefig("plot2.jpeg")