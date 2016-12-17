import numpy
from sklearn.preprocessing import MinMaxScaler

# My function without sklearn
def featureScaling(arr):
    x_min = numpy.amin(arr)
    x_max = numpy.amax(arr)
    new_features = []
    for e in arr:
        if (x_min == x_max):
            x = 0.5
        else:
            x = (e - x_min) / (x_max - x_min)
        new_features.append(x)
    return new_features

# My function with sklearn
def easierFS(arr):
    weights = numpy.array(arr)
    rescaled_weights = MinMaxScaler().fit_transform(weights)
    return rescaled_weights

data = [115., 140., 175.]
print featureScaling(data)
print easierFS(data)
