import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

def create_data(points, classes):
    X = np.zeros((points*classes, 2))
    Y = np.zeros((points*classes, 2))
    for class_number in range(classes):
        ix = range(points*class_number, points*(class_number+1))
        r = np.linspace(0.0, 1, points)
        t = np,linspace(class_number * 4, (class_number+1) * 4, points) + np.random.randn(points) * 0.2
        X[ix] = np.c_[r*]



class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


layer1 = Layer_Dense(4, 5)
layer2= Layer_Dense(5, 2)

layer1.forward(X)
layer2.forward(layer1.output)
print(layer2.output)
