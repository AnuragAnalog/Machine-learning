#!/usr/bin/python3

class Node():
    def __init__(self, value):
        self.value = value
        self.cluster_no = -1

    def __str__(self):
        if self.cluster_no == -1:
            return "Node is not yet assigned to any cluster"
        else:
            return "Node belongs to cluster no: "+str(self.cluster_no)

    def get_value(self):
        return self.value

    def get_cluster(self):
        return self.cluster_no

    def set_cluster(self, cluster_no):
        self.cluster_no = cluster_no