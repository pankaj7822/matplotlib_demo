import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
 
# Dataset
blue_y=np.array([20, 15, 5, 12, 39, 48,30,28,26,27,47,39,20])
black_y=np.array([20, 18, 6, 12, 39, 48,34,32,30,31,47,39,20])
red_y=np.array([20, 15, 5, 12, 39, 48,32,30,28,29,49,41,20])
yellow_y=np.array([20, 18, 6, 12, 39, 48,36,34,29,28,47,39,20])
x=np.array([i+1 for i in range(len(blue_y))])
 
cubic_interploation_model_blue = interp1d(x, blue_y, kind = "cubic")
cubic_interploation_model_black = interp1d(x, black_y, kind = "cubic")
cubic_interploation_model_red = interp1d(x, red_y, kind = "cubic")
cubic_interploation_model_yellow = interp1d(x, yellow_y, kind = "cubic")

# Plotting the Graph
X_=np.linspace(x.min(), x.max(), 500)
Blue_Y_=cubic_interploation_model_blue(X_)
Black_Y_=cubic_interploation_model_black(X_)
Red_Y_=cubic_interploation_model_red(X_)
Yellow_Y_=cubic_interploation_model_yellow(X_)

 
plt.plot(X_, Blue_Y_,color="blue",label="Base load curve")
plt.plot(X_, Black_Y_,color="black",label="Load curve under electricity price e(1)")
plt.plot(X_, Red_Y_,color="red",linestyle='dashed',label="Load curve under electricity price e(2)")
plt.plot(X_, Yellow_Y_,color="yellow",label="Load curve under electricity price e(3) ")
plt.legend()
plt.title("Power Vs Time")
plt.xlabel("Time")
plt.ylabel("Power Load")
plt.savefig("plot1.jpeg")