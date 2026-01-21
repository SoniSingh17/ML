import numpy as np
from collections import Counter


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))



class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = []
        for x in X:
            predictions.append(self._predict_single(x))
        return np.array(predictions)

    def _predict_single(self, x):
        # Compute distances
        distances = []
        for i in range(len(self.X_train)):
            dist = euclidean_distance(x, self.X_train[i])
            distances.append((dist, self.y_train[i]))

        # Sort by distance
        distances.sort(key=lambda x: x[0])

        # Select k nearest labels
        k_nearest_labels = [label for (_, label) in distances[:self.k]]

        # Majority vote
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]
