# from Patrick Loeber
import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:

    def __init__(self, lr=1.925, n_iters=132): # lr is learning rate, n_iters is number of iterations
        self.lr = lr
        self.n_iters = n_iters
        self.weights = None
        self.bias = None

    def fit(self, X, y): # X is a multivariable vector, y is a vector
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        iteration = np.zeros(self.n_iters)
        costY = np.zeros(self.n_iters)

        for i in range(self.n_iters):
            y_predicted = np.dot(X, self.weights) + self.bias

            dw = (1/n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1/n_samples) * np.sum(y_predicted - y)
            
            iteration[i] = i
            costY[i] = (1/n_samples) * np.sum((y_predicted - y)**2)
            
            self.weights -= self.lr * dw
            self.bias -= self.lr * db

        plt.plot(iteration, costY)
        plt.show()

    def predict(self, X):
        y_predicted = np.dot(X, self.weights) + self.bias
        return y_predicted
