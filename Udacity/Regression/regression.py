from sklearn import linear_model
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

diabetes_input = diabetes.data[:, np.newaxis, 2]

diabetes_input_train = diabetes_input[:-20]
diabetes_input_test = diabetes_input[-20:]

diabetes_output_train = diabetes.target[:-20]
diabetes_output_test = diabetes.target[-20:]

reg = linear_model.LinearRegression()

reg.fit(diabetes_input_train, diabetes_output_train)

print('Slope: ', reg.coef_)
print('Intercept: ',reg.intercept_)

# Squared error
error = np.mean((reg.predict(diabetes_input_test) - diabetes_output_test ** 2))
print('Error: ', error)

# Plot output
plt.scatter(diabetes_input_test, diabetes_output_test, color='red')
plt.plot(diabetes_input_test, reg.predict(diabetes_input_test), color='blue', linewidth=3)

plt.xticks()
plt.yticks()

plt.show()
