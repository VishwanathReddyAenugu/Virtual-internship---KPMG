import numpy as np
from kmodes.kmodes import KModes
import pandas as pd


data = pd.read_csv("Final.csv")

# km = KModes(n_clusters=4, init='Huang', n_init=5, verbose=1)
#
# clusters = km.fit_predict(data)
#
# # Print the cluster centroids
# print(km.cluster_centroids_)