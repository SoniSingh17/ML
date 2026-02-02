import math

class LogisticRegressionScratch:
    def __init__(self, lr=0.01, epochs=1000):
        self.lr = lr
        self.epochs = epochs
        self.w = []
        self.b = 0

    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def fit(self, X, y):
        n_samples = len(X)
        n_features = len(X[0])

        # initialize weights
        self.w = [0] * n_features
        self.b = 0

        for _ in range(self.epochs):
            dw = [0] * n_features
            db = 0

            for i in range(n_samples):
                z = sum(self.w[j] * X[i][j] for j in range(n_features)) + self.b
                y_pred = self.sigmoid(z)

                error = y_pred - y[i]

                for j in range(n_features):
                    dw[j] += error * X[i][j]

                db += error

            # update parameters
            for j in range(n_features):
                self.w[j] -= self.lr * dw[j] / n_samples

            self.b -= self.lr * db / n_samples

    def predict(self, X):
        predictions = []
        for x in X:
            z = sum(self.w[j] * x[j] for j in range(len(x))) + self.b
            y_pred = self.sigmoid(z)
            predictions.append(1 if y_pred >= 0.5 else 0)
        return predictions
