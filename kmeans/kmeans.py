#!/usr/bin/python3

import numpy as np
import pandas as pd

class kMeans():
    def __init__(self, k_clusters, iterate=20):
        self.clusters = k_clusters
        self.centroids = list()
        self.iterations = iterate
        self.cluster_names = dict()

    def __str__(self):
        return "kMeans(clusters: "+str(self.clusters)+")"

    def __encode_to_clusters(self, labels):
        enum_labels = list(enumerate(labels))

        for mapping in enum_labels:
            self.cluster_names[str(mapping[0])] = mapping[1]
        return

    def cluster(self):
        pass