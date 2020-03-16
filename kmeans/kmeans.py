#!/usr/bin/python3

import numpy as np
import pandas as pd

from node import Node

class kMeans():
    def __init__(self, k_clusters, iterate=20):
        self.clusters = k_clusters
        self.centroids = dict()
        self.iterations = iterate
        self.cluster_names = dict()
        self.data_length = 0

    def __str__(self):
        return "kMeans(clusters: "+str(self.clusters)+")"

    def __encode_to_clusters(self, labels):
        # Enumerate label names

        enum_labels = list(enumerate(labels))

        for mapping in enum_labels:
            self.cluster_names[str(mapping[0])] = mapping[1]
        return

    def __random_initialize(self, data):
        initial_points = list()

        for c in range(self.clusters):
            index = np.random.randint(self.data_length)
            tmp = data[index]
            tmp.set_cluster(c)
            initial_points.append(tmp)

        return initial_points

    def __euclidian_dist(self, point1, point2):
        dist = 0
        for (p1, p2) in zip(point1, point2):
            dist += (p1 - p2) * (p1 - p2)
        dist = np.sqrt(dist)

        return dist

    def __calculate_centroids(self, data):
        pass

    def get_encoding(self):
        return self.cluster_names

    def total_cluster_variance(self, data):
        pass

    def within_cluster_variance(self, data, cluster_no):
        pass

    def fit(self, X, labels=None):
        """
        Parameters
        ----------
        X : ndarray, list
            A n-d array which represents the data

        Returns
        -------
        None : NoneType
        """

        self.data_length = len(X)

        if labels is not None:
            uniq_labels = list(set(labels))
            self.__encode_to_clusters(uniq_labels)

        tmp_data = list()
        for point in X.values:
            tmp_data.append(Node(point))

        for _ in range(self.iterations):
            centroids = self.__random_initialize(tmp_data)

            while True:
                for i in range(self.data_length):
                    for j in range(self.clusters):
                        centroid = centroids[j]

        return

    def predict(self, y_new):
        pass

if __name__ == '__main__':
    data = pd.read_csv('dataset.csv')

    cluster = kMeans(2)

    cluster.fit(data.values)
    cluster.predict([3, 40])