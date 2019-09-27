from knn import KNN
import matplotlib.pyplot as plt
import numpy as np

knn = KNN()

knn.Load_Dataset('iris.csv')

x = knn.data[:, 0]
y = knn.data[:, 1]

trainX = knn.data[::2, 1:3]
trainy = knn.target[::2]

testX = knn.data[1::2, 1:3]
testy = knn.target[1::2]

colors = np.zeros((3, 3), dtype='f')
colors[0, :] = [1, 0.5, 0.5]
colors[1, :] = [0.5, 1, 0.5]
colors[2, :] = [0.5, 0.5, 1]

plt.figure()
[numItems, numFeatures] = knn.data.shape

knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
for i in range(0, len(testX)):
    actualClass = testy[i]
    prediction = knn.Predict(testX[i, 0:2])
    print(actualClass, prediction)

for i in range(0, numItems / 2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass, :]
    plt.scatter(trainX[i, 0], trainX[i, 1], facecolor=currColor, lw=2)

predRight = 0
for i in range(0, numItems / 2):
    actualClass = testy[i]
    itemClass = int(testy[i])
    currColor = colors[itemClass, :]
    prediction = int(knn.Predict(testX[i, :]))
    if prediction == actualClass:
        predRight += 1
    edgeColor = colors[prediction, :]
    plt.scatter(testX[i, 0], testX[i, 1], facecolor=currColor, edgecolor=edgeColor, lw=2)

print (predRight / 75.) * 100

plt.show()
