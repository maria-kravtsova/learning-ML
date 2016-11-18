from sklearn.svm import SVC
from sklearn import datasets

iris = datasets.load_iris()

clf = SVC(kernel='linear')
clf.fit(iris.data, iris.target)
prediction = clf.predict(iris.data)
print(prediction)
accuracy = clf.score(iris.data, iris.target)
print(accuracy)
