#load the image 
# convert the image into hsv scale
# perform the k-means cluster 

import numpy as np
import cv2 
import os
import utilities

colors = ["blue", "red", "orange", "purple"]

def k_means_cluster(points,k, epsilon = 0.01, clusters = None):
    if clusters == None: clusters = pick_points(points,k)
    labels = np.empty((len(points),1))
    new_clusters = np.empty((len(clusters), 1))

    while np.linalg.norm(clusters - new_clusters) > epsilon:
        distances = np.linalg.norm(points[:, np.newaxis] - clusters, axis=2)
        
        closest_clusters = np.argmin(distances, axis=1)
        
        labels = np.array(colors)[closest_clusters]

        new_clusters = np.array([np.average(points[closest_clusters == i], axis=0) for i in range(k)])
        
    return clusters,labels

def pick_points(points, k):
    return points[np.random.choice(range(len(points)), k, replace=False)]
def distance(p1, p2):
    return np.linalg.norm(p1-p2) 

def mini_batch(points,k,batch_size = 8, epochs = 100):
    clusters = None
    for i in range(epochs):
        for j in range(batch_size):
            index = int(len(points)/batch_size)
            batch_points = points[index:k+index]
            labels, clusters = k_means_cluster(points, clusters=clusters)




# read the image 
img = cv2.imread(os.path.join(os.getcwd(), 'color_clustering', 'image.png'))
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
flattened_array = hsv_img.reshape(-1, 3)

clusters, labels = k_means_cluster(flattened_array, 4)