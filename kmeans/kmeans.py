#!/usr/bin/python3

import numpy as np
import pandas as pd

class kMeans():
    def __init__(self, k_clusters, iterate=20):
        self.clusters = k_clusters
        self.centroids = list()
        self.iterations = iterate

    def __str__(self):
        return "kMeans(clusters: "+str(self.clusters)+")"

    def cluster(self):
        pass