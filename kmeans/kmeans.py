#!/usr/bin/python3

import numpy as np
import pandas as pd

from node import Node

class kMeans():
    def __init__(self, k_clusters, iterate=20):
        self.clusters = k_clusters
        self.centroids = dict()
        self.iterations = iterate
        self.data_length = 0

    def __str__(self):
        return "kMeans(clusters: "+str(self.clusters)+")"

    def __random_initialize(self, data):
        # Randomly select the nodes

        initial_points = list()

        for c in range(self.clusters):
            index = np.random.randint(self.data_length)
            tmp = data[index]
            tmp.set_cluster(c)
            initial_points.append(tmp)

        return initial_points

    def __euclidian_dist(self, point1, point2):
        # calculate the euclidian distance between two points

        dist = 0
        for (p1, p2) in zip(point1, point2):
            dist += (p1 - p2) * (p1 - p2)
        dist = np.sqrt(dist)

        return dist

    def __calculate_centroids(self, data):
        # calculate the centroids after clustering through one iteration

        size_of_clusters = [0 for i in range(self.clusters)]
        centroids = [[0 for i in range(len(data[0]))] for j in range(self.clusters)]

        for i in range(self.data_length):
            cluster = data[i].get_cluster()
            value = data[i].get_value()
            for j in range(len(value)):
                centroids[cluster][j] += value[j]
            size_of_clusters[cluster] += 1

        for i in range(self.clusters):
            for j in range(len(data[0])):
                centroids[i][j] /= size_of_clusters[j]
            self.centroids[str(i)] = centroids[i]

        return

    def total_cluster_variance(self, data):
        """
        Parameters
        ----------
        data : list
            It's a list a points, which belongs to the class Node

        Returns
        -------
        total_var : float
            Variance of the entire dataset
        """

        total_var = 0

        for cluster in range(self.clusters):
            total_var += self.within_cluster_variance(data, cluster)

        return total_var

    def within_cluster_variance(self, data, cluster_no):
        """
        Parameters
        ----------
        data : list
            It's a list a points, which belongs to the class Node
        cluster_no : int
            Specifies the cluster number

        Returns
        -------
        var : float
            Variance of the specified cluster
        """

        var = 0
        size = 0
        centroid = self.centroids[str(cluster_no)].get_value()

        for i in range(len(data)):
            if data[i].get_cluster() == cluster_no:
                var += self.__euclidian_dist(centroid, data[i].get_value())

        var /= size

        return var

    def converge_to_centroid(self, data, initial_points):
        pre_var = None
        cur_var = 0

        while pre_var != cur_var:
            for i in range(self.data_length):
                val = np.inf
                ind = 0
                for j in range(self.clusters):
                    centroid = initial_points[j]
                    dist = self.__euclidian_dist(data[i].get_value(), centroid.get_value())
                    if val > dist:
                        val = dist
                        ind = j
                data[i].set_cluster(initial_points[ind].get_cluster())

            self.__calculate_centroids(data)
            pre_var = cur_var
            cur_var = self.total_cluster_variance(data)

    def fit(self, X):
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

        tmp_data = list()
        for point in X.values:
            tmp_data.append(Node(point))

        for _ in range(self.iterations):
            centroids = self.__random_initialize(tmp_data)

            self.converge_to_centroid(tmp_data, centroids)

        return

    def predict(self, y_new):
        """
        Parameters
        ----------
        y_new : list
            A new point to be predicted

        Returns
        -------
        ind : int
            Predicted cluster number it belongs to
        name : str
            Predicted cluster name, if defined
        """

        mini = np.inf
        ind = 0
        for i in range(self.clusters):
            dist = self.__euclidian_dist(self.centroids[str(i)], y_new)

            if mini > dist:
                mini = dist
                ind = i

        return ind

if __name__ == '__main__':
    data = pd.read_csv('dataset.csv')

    cluster = kMeans(2)

    cluster.fit(data.values)
    cluster.predict([3, 40])