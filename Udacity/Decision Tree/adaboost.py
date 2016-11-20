from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier

iris = load_iris()
clf = AdaBoostClassifier(n_estimators=100)
clf = clf.fit(iris.data, iris.target)
prediction = clf.predict(iris.data)

accuracy = clf.score(iris.data, iris.target, sample_weight=None)
print('accuracy is ', accuracy)
