from sklearn.linear_model import Ridge
import pandas as pd

class TriFiLearn:

	def __init__(self):
		print "requesting x training set"
		# setX = pd.read_csv("http://localhost:8080/csv/dimension/x/version/floor10-test")
		setX = pd.read_csv("csv/training-set-x-version-floor10-test.csv")
		labelsX = setX['x'].values
		featuresX = setX.iloc[:, 1:].values
		self.modelX = Ridge(normalize=True).fit(featuresX, labelsX)

		print "requesting y training set"
		# setY = pd.read_csv("http://localhost:8080/csv/dimension/y/version/floor10-test")
		setY = pd.read_csv("csv/training-set-y-version-floor10-test.csv")
		labelsY = setY['y'].values
		featuresY = setY.iloc[:, 1:].values
		self.modelY = Ridge(normalize=True).fit(featuresY, labelsY)

	def predictX(self, features):
		return self.modelX.predict(features)

	def predictY(self, features):
		return self.modelY.predict(features)

	def trainX(self, label, features):
		labelsX.append(label)
		featuresX.append(features)
		self.modelX = Ridge(normalize=True).fit(featuresX, labelsX)

	def trainY(self, label, features):
		labelsY.append(label)
		featuresY.append(features)
		self.modelY = Ridge(normalize=True).fit(featuresY, labelsY)

	def reset(self):
		self.__init__()