import numpy as np
import pickle
from knn import KNN

knn = KNN()


def ReshapeData(set1, set2):
    X = np.zeros((2000, 5 * 2 * 3), dtype='f')
    y = np.zeros(2000, dtype='f')
    for row in range(0, 1000):
        y[row] = 5
        y[row + 1000] = 6
        col = 0
        for j in range(0, 5):
            for k in range(0, 2):
                for m in range(0, 3):
                    X[row, col] = set1[j, k, m, row]
                    X[row + 1000, col] = set2[j, k, m, row]
                    col = col + 1
    return X, y


def ReduceData(X):
    X = np.delete(X, 1, 1)
    X = np.delete(X, 1, 1)
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)
    X = np.delete(X, 0, 2)
    return X


def CenterData(X):
    allXCoordinates = X[:, :, 0, :]
    meanValue = allXCoordinates.mean()
    X[:, :, 0, :] = allXCoordinates - meanValue

    allYCoordinates = X[:, :, 1, :]
    meanValueY = allYCoordinates.mean()
    X[:, :, 1, :] = allXCoordinates - meanValueY
    return X


test5_in = open("userData/test5.p", "rb")
test5 = pickle.load(test5_in)


test6_in = open("userData/test6.p", "rb")
test6 = pickle.load(test6_in)

train5_in = open("userData/train5.p", "rb")
train5 = pickle.load(train5_in)

train6_in = open("userData/train6.p", "rb")
train6 = pickle.load(train6_in)

train5 = ReduceData(train5)
train6 = ReduceData(train6)
test5 = ReduceData(test5)
test6 = ReduceData(test6)

train5 = CenterData(train5)
train6 = CenterData(train6)
test5 = CenterData(test5)
test6 = CenterData(test6)

trainX, trainy = ReshapeData(train5, train6)
testX, testy = ReshapeData(test5, test6)

knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
predRight = 0
for row in range(0, 2000):
    prediction = int(knn.Predict(testX[row, :]))
    actual = int(testy[row])
    if prediction == actual:
        predRight += 1
    else:
        print row
        print prediction, actual

percentage = (predRight / 2000.) * 100
# print testX
# print testy

print predRight
print percentage
