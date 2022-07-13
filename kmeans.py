import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('data.csv')
from sklearn.cluster import KMeans
import numpy as np
# k means
kmeans = KMeans(n_clusters=5, random_state=0)
df['cluster'] = kmeans.fit_predict(df[['X', 'Y']])
# get centroids
centroids = kmeans.cluster_centers_
print(centroids)
cen_x = [i[0] for i in centroids] 
cen_y = [i[1] for i in centroids]
## add to df
df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2],3:cen_x[3],4:cen_x[4]})
df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2],3:cen_y[3],4:cen_y[4]})
# define and map colors
colors = ['#DF2020', '#81DF20', '#2095DF','#FF33D4', '#CAC728']
df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2],3:colors[3], 4:colors[4]})
plt.scatter(df.X, df.Y, c=df.c, alpha = 0.6, s=10)
plt.savefig("t.png")
plt.close()

from scipy.spatial import ConvexHull
import numpy as np
fig, ax = plt.subplots(1, figsize=(8,8))
# plot data
plt.scatter(df.X, df.Y, c=df.c, alpha = 0.6, s=10)
# plot centers
plt.scatter(cen_x, cen_y, marker='^', c=colors, s=70)
# draw enclosure
for i in df.cluster.unique():
    points = df[df.cluster == i][['X', 'Y']].values
    # get convex hull
    hull = ConvexHull(points)
    # get x and y coordinates
    # repeat last point to close the polygon
    x_hull = np.append(points[hull.vertices,0],
                       points[hull.vertices,0][0])
    y_hull = np.append(points[hull.vertices,1],
                       points[hull.vertices,1][0])
    # plot shape
    plt.fill(x_hull, y_hull, alpha=0.3, c=colors[i])
    
plt.xlim(0,100)
plt.ylim(0,100)
plt.savefig("t2.png")