from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
prediction = clf.predict(iris.data)

accuracy = clf.score(iris.data, iris.target, sample_weight=None)
print('accuracy is ', accuracy)
