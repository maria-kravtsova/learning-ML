from sklearn.naive_bayes import GaussianNB
from sklearn import datasets

iris = datasets.load_iris()

# create a classifier
clf = GaussianNB()
# feed the input and output
clf.fit(iris.data, iris.target)
# test the data with predict function
prediction = clf.predict(iris.data)

accuracy = clf.score(iris.data, iris.target, sample_weight=None)
print('accuracy is ', accuracy)
