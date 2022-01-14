# CICS 397A Lab 10/13
#
# Complete the following bits of code where indicated in the comments.  Be mindful of function 
# parameters and expected return types.


import math
import csv
from itertools import combinations

# Data snippet:
#
# state,2016D,2016R,2012D,2012R,2008D,2008R,2004D,2004R,2000D,2000R,1996D,1996R,1992D,1992R,1988D,1988R
# Alabama,34.36,62.08,38.36,60.55,38.74,60.32,36.84,62.46,41.57,56.48,43.16,50.12,40.88,47.64,39.86,59.17
# Alaska,36.55,51.28,40.81,54.8,37.89,59.42,35.52,61.07,27.67,58.62,33.27,50.8,30.29,39.46,36.27,59.59
def read_state_data(infile_path):
    """Read in the US Presidential election data.

    Returns: a dictionary with state names as keys, and lists of voting percentages as values.

    """
    state_data = {}
    with open(infile_path, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            # state_data[row[0]] = [float(row[i]) - float(row[i+1]) for i in range(1, len(row), 2)]
            state_data[row[0]] = [ float(r) for r in row[1:] ]  
    return state_data


def print_state_clusters(clusters):
    """Pretty print a set of state clusters based on the election data."""
    for cluster in clusters:
        x_tot = 0.0
        for c in cluster:
            data = instance_data[c]  # similar to dist funcs, we assume this exists

            # use the average diff between D and R to summarize
            x = sum([ data[i] - data[i+1] for i in range(0, len(data), 2) ]) / (len(data)/2)
            x_tot += x
        score = x_tot / len(cluster)
        prefix = " "*(50 - int(score))
        for c in cluster:
            print(prefix, c)
        print("")  


# These distance function take single elements of clusters and calculate their distance.  They 
# assume the existence of the instance_data dictionary name => [ val1, val2, val3, ...]
instance_data = dict()  # THIS MUST GET ASSIGNED SOMEWHERE BELOW!

def dist_euclidean(c1, c2):
    """Return the geometric distance between two cluster elements."""
    row1, row2 = instance_data[c1], instance_data[c2]
    #
    # Fill this in!
    #
    return math.sqrt((row1 - row2) * (row1 - row2))


def dist_alphabetical(c1, c2):
    """Return the ASCII distance between the first letter of the elements."""
    return abs(ord(c1[0]) - ord(c2[0]))


def avg_link_dist(cluster1, cluster2, dist_func):
    """Calculate cluster distance based on the average distance between all pairs in each.
        
    Args:
        cluster1: a tuple representing a single cluster
        cluster2: a tuple representing a different cluster
        dist_func: A function that takes two individual cluster elements and returns their distance

    Returns:
        A number representing the average distance between the instances in each cluster
    """
    #
    # Fill this in!
    #
    result = 0
    for instance_data in cluster1:
        distance = dist_func(cluster1, cluster2)
        result = result + distance
    result = result / len(cluster1)
    return result


def single_link_dist(cluster1, cluster2, dist_func):
    """Calculate cluster distance based on the smallest distance between any node in the first
    cluster and any node in the second cluster.
        
    Args:
        cluster1: a tuple representing a single cluster
        cluster2: a tuple representing a different cluster
        dist_func: A function that takes two individual cluster elements and returns their distance

    Returns:
        A number representing the minimum distance between any pair of instances from each cluster

    """
    dist_min = 1.0
    for c1 in cluster1:
        for c2 in cluster2:
            dist_min = min(dist_min, dist_func(c1, c2))
    return dist_min


def complete_link_dist(cluster1, cluster2, dist_func):
    """Calculate cluster distance based on the longest distance between any node in the first
    cluster and any node in the second cluster.
        
    Args:
        cluster1: a tuple representing a single cluster
        cluster2: a tuple representing a different cluster
        dist_func: A function that takes two individual cluster elements and returns their distance

    Returns:
        A number representing the maximum distance between any pair of instances from each cluster

    """
    longest_distance = 0
    for i in cluster1:
        for j in cluster2:
            if longest_distance < dist_func(cluster1[i], cluster2[j]):
                longest_distance = dist_func(cluster1[i], cluster2[j])
    
    return longest_distance


def closest_pair(clusters, cluster_dist_func, instance_dist_func):
    """Return the pair of clusters with the smallest cluster distance between them.
    
    Args:
        clusters: a list or set of clusters represented as tuples
        cluster_dist_func: A function that takes a two clusters and returns the distance
        instance_dist_func: A function that takes two individual instances and returns the distance
    
    Returns:
        A 2-element tuple containing the two clusters that are closest together 
    
    """
    best_dist = math.inf
    best_pair = (None, None)    
    for cluster1, cluster2 in combinations(clusters, 2):
        dist = cluster_dist_func(cluster1, cluster2, instance_dist_func)
        if  dist < best_dist:
            best_pair = (cluster1, cluster2)
            best_dist = dist
    return best_pair


def agglomerative(instances, cluster_dist_func, instance_dist_func, verbose=False):
    """Perform agglomerative hierarchical clustering.
    
    Args:
        instances: a list of set of elements that will be clustered together
        cluster_dist_func: A function that takes a two clusters and returns the distance
        instance_dist_func: A function that takes two individual instances and returns the distance
    
    Returns:
        A list of clusterings, one per iteration of the alorithm.  The last item in this list will contain
        a single cluster that has all the instances.
    """
    clusters = { (x,) for x in instances }
    cluster_iterations = []  # list of sets of tuples - complete clustering at each iter 
    for iter in range(len(clusters) - 1):
        cluster1, cluster2 = closest_pair(clusters, cluster_dist_func, instance_dist_func)
        clusters.remove(cluster1)
        clusters.remove(cluster2)
        clusters.add(cluster1 + cluster2)

        if verbose:
            print("iter {}:".format(iter))
            for cluster in clusters:
                print("\t", cluster)
            print("\n")

        cluster_iterations.append(clusters.copy())    
    return cluster_iterations


#####################################

if __name__ == '__main__':

    instance_data = read_state_data(r"C:\Users\aaron\Desktop\397A_Lab1013\1988-2016.csv")
    cluster_iters = agglomerative(instance_data.keys(), single_link_dist, dist_alphabetical)
    print_state_clusters(cluster_iters[44])






