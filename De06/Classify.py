import numpy as np
import pickle
from knn import KNN

knn = KNN()


def ReshapeData(set1, set2, set3, set4, set5, set6, set7, set8, set9, set10, set11, set12, set13, set14, set15, set16,
                set17, set18, set19, set20, set21, set22, set23, set24, set25, set26, set27):
    X = np.zeros((27000, 5 * 2 * 3), dtype='f')
    y = np.zeros(27000, dtype='f')
    for row in range(0, 1000):
        y[row] = 0
        y[row + 1000] = 1
        y[row + 2000] = 2
        y[row + 3000] = 3
        y[row + 4000] = 4
        y[row + 5000] = 5
        y[row + 6000] = 6
        y[row + 7000] = 7
        y[row + 8000] = 8
        y[row + 9000] = 9
        y[row + 10000] = 0
        y[row + 11000] = 5
        y[row + 12000] = 6
        y[row + 13000] = 1
        y[row + 14000] = 3
        y[row + 15000] = 4
        y[row + 16000] = 7
        y[row + 17000] = 8
        y[row + 18000] = 9
        y[row + 19000] = 2
        y[row + 20000] = 4
        y[row + 21000] = 7
        y[row + 22000] = 9
        y[row + 23000] = 6
        y[row + 24000] = 7
        y[row + 25000] = 8
        y[row + 26000] = 6
        col = 0
        for j in range(0, 5):
            for k in range(0, 2):
                for m in range(0, 3):
                    X[row, col] = set1[j, k, m, row]
                    X[row + 1000, col] = set2[j, k, m, row]
                    X[row + 2000, col] = set3[j, k, m, row]
                    X[row + 3000, col] = set4[j, k, m, row]
                    X[row + 4000, col] = set5[j, k, m, row]
                    X[row + 5000, col] = set6[j, k, m, row]
                    X[row + 6000, col] = set7[j, k, m, row]
                    X[row + 7000, col] = set8[j, k, m, row]
                    X[row + 8000, col] = set9[j, k, m, row]
                    X[row + 9000, col] = set10[j, k, m, row]
                    X[row + 10000, col] = set11[j, k, m, row]
                    X[row + 11000, col] = set12[j, k, m, row]
                    X[row + 12000, col] = set13[j, k, m, row]
                    X[row + 13000, col] = set14[j, k, m, row]
                    X[row + 14000, col] = set15[j, k, m, row]
                    X[row + 15000, col] = set16[j, k, m, row]
                    X[row + 16000, col] = set17[j, k, m, row]
                    X[row + 17000, col] = set18[j, k, m, row]
                    X[row + 18000, col] = set19[j, k, m, row]
                    X[row + 19000, col] = set20[j, k, m, row]
                    X[row + 20000, col] = set21[j, k, m, row]
                    X[row + 21000, col] = set22[j, k, m, row]
                    X[row + 22000, col] = set23[j, k, m, row]
                    X[row + 23000, col] = set24[j, k, m, row]
                    X[row + 24000, col] = set25[j, k, m, row]
                    X[row + 25000, col] = set26[j, k, m, row]
                    X[row + 26000, col] = set27[j, k, m, row]
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
    X[:, :, 1, :] = allYCoordinates - meanValueY
    return X


test5_in = open("userData/Peck_test5.p", "rb")
test5 = pickle.load(test5_in)

test6_in = open("userData/MacMaster_test6.p", "rb")
test6 = pickle.load(test6_in)

train5_in = open("userData/Peck_train5.p", "rb")
train5 = pickle.load(train5_in)

train6_in = open("userData/MacMaster_train6.p", "rb")
train6 = pickle.load(train6_in)

test0 = pickle.load(open('userData/Soccorsi_test0.p', "rb"))
train0 = pickle.load(open('userData/Soccorsi_train0.p', 'rb'))

test1 = pickle.load(open('userData/Giroux_test1.p', 'rb'))
train1 = pickle.load(open('userData/Giroux_train1.p', 'rb'))

test2 = pickle.load(open('userData/Newton_test2.p', 'rb'))
train2 = pickle.load(open('userData/Newton_train2.p', 'rb'))

test3 = pickle.load(open('userData/Trinity_test3.p', 'rb'))
train3 = pickle.load(open('userData/Trinity_train3.p', 'rb'))

test4 = pickle.load(open('userData/Beaulieu_test4.p', 'rb'))
train4 = pickle.load(open('userData/Beaulieu_train4.p', 'rb'))

test7 = pickle.load(open('userData/Erickson_test7.p', 'rb'))
train7 = pickle.load(open('userData/Erickson_train7.p', 'rb'))

test8 = pickle.load(open('userData/Erickson_test8.p', 'rb'))
train8 = pickle.load(open('userData/Erickson_train8.p', 'rb'))

test9 = pickle.load(open('userData/Soccorsi_test9.p', 'rb'))
train9 = pickle.load(open('userData/Soccorsi_train9.p', 'rb'))

test5b = pickle.load(open('userData/Boland_test5.p', 'rb'))
train5b = pickle.load(open('userData/Boland_train5.p', 'rb'))

test0b = pickle.load(open('userData/Clark_test0.p', 'rb'))
train0b = pickle.load(open('userData/Clark_train0.p', 'rb'))

test6b = pickle.load(open('userData/Boland_test6.p', 'rb'))
train6b = pickle.load(open('userData/Boland_train6.p', 'rb'))

test1b = pickle.load(open('userData/Clark_test1.p', 'rb'))
train1b = pickle.load(open('userData/Clark_train1.p', 'rb'))

test3b = pickle.load(open('userData/Beatty_test3.p', 'rb'))
train3b = pickle.load(open('userData/Beatty_train3.p', 'rb'))

test4b = pickle.load(open('userData/Warren_test4.p', 'rb'))
train4b = pickle.load(open('userData/Warren_train4.p', 'rb'))

test7b = pickle.load(open('userData/Zhang_test7.p', 'rb'))
train7b = pickle.load(open('userData/Zhang_train7.p', 'rb'))

test8b = pickle.load(open('userData/Zhang_test8.p', 'rb'))
train8b = pickle.load(open('userData/Zhang_train8.p', 'rb'))

test9b = pickle.load(open('userData/Saulean_test9.p', 'rb'))
train9b = pickle.load(open('userData/Saulean_train9.p', 'rb'))

test2b = pickle.load(open('userData/Cottrell_test2.p', 'rb'))
train2b = pickle.load(open('userData/Cottrell_train2.p', 'rb'))

test4c = pickle.load(open('userData/Deluca_test4.p', 'rb'))
train4c = pickle.load(open('userData/Deluca_train4.p', 'rb'))

test7c = pickle.load(open('userData/Huang_test7.p', 'rb'))
train7c = pickle.load(open('userData/Huang_train7.p', 'rb'))

test9c = pickle.load(open('userData/Lee_test9.p', 'rb'))
train9c = pickle.load(open('userData/Lee_train9.p', 'rb'))

test6c = pickle.load(open('userData/Wu_test6.p', 'rb'))
train6c = pickle.load(open('userData/Wu_train6.p', 'rb'))

test7d = pickle.load(open('userData/Mardis_test7.p', 'rb'))
train7d = pickle.load(open('userData/Mardis_train7.p', 'rb'))

test8c = pickle.load(open('userData/Mardis_test8.p', 'rb'))
train8c = pickle.load(open('userData/Mardis_train8.p', 'rb'))

test6d = pickle.load(open('userData/Picard_test6.p', 'rb'))
train6d = pickle.load(open('userData/Picard_train6.p', 'rb'))



train5 = ReduceData(train5)
train6 = ReduceData(train6)
test5 = ReduceData(test5)
test6 = ReduceData(test6)
train2 = ReduceData(train2)
test2 = ReduceData(test2)
train3 = ReduceData(train3)
test3 = ReduceData(test3)
train0 = ReduceData(train0)
test0 = ReduceData(test0)
train1 = ReduceData(train1)
test1 = ReduceData(test1)
train4 = ReduceData(train4)
test4 = ReduceData(test4)
train7 = ReduceData(train7)
test7 = ReduceData(test7)
train8 = ReduceData(train8)
test8 = ReduceData(test8)
train9 = ReduceData(train9)
test9 = ReduceData(test9)

test0b = ReduceData(test0b)
train0b = ReduceData(train0b)
train1b = ReduceData(train1b)
test1b = ReduceData(test1b)
train2b = ReduceData(train2b)
test2b = ReduceData(test2b)
train3b = ReduceData(train3b)
test3b = ReduceData(test3b)
train4b = ReduceData(train4b)
test4b = ReduceData(test4b)
train4c = ReduceData(train4c)
test4c = ReduceData(test4c)
test5b = ReduceData(test5b)
train5b = ReduceData(train5b)
test6b = ReduceData(test6b)
train6b = ReduceData(train6b)
test6c = ReduceData(test6c)
train6c = ReduceData(train6c)
test6d = ReduceData(test6d)
train6d = ReduceData(train6d)
test7b = ReduceData(test7b)
train7b = ReduceData(train7b)
test7c = ReduceData(test7c)
train7c = ReduceData(train7c)
test7d = ReduceData(test7d)
train7d = ReduceData(train7d)
test8b = ReduceData(test8b)
train8b = ReduceData(train8b)
test8c = ReduceData(test8c)
train8c = ReduceData(train8c)
test9b = ReduceData(test9b)
train9b = ReduceData(train9b)
test9c = ReduceData(test9c)
train9c = ReduceData(train9c)

train5 = CenterData(train5)
train6 = CenterData(train6)
test5 = CenterData(test5)
test6 = CenterData(test6)
train2 = CenterData(train2)
test2 = CenterData(test2)
train3 = CenterData(train3)
test3 = CenterData(test3)
test0 = CenterData(test0)
train0 = CenterData(train0)
test1 = CenterData(test1)
train1 = CenterData(train1)
test4 = CenterData(test4)
train4 = CenterData(train4)
test7 = CenterData(test7)
train7 = CenterData(train7)
test8 = CenterData(test8)
train8 = CenterData(train8)
test9 = CenterData(test9)
train9 = CenterData(train9)

test0b = CenterData(test0b)
train0b = CenterData(train0b)
test1b = CenterData(test1b)
train1b = CenterData(train1b)
test2b = CenterData(test2b)
train2b = CenterData(train2b)
test3b = CenterData(test3b)
train3b = CenterData(train3b)
test4b = CenterData(test4b)
train4b = CenterData(train4b)
test4c = CenterData(test4c)
train4c = CenterData(train4c)
test5b = CenterData(test5b)
train5b = CenterData(train5b)
test6b = CenterData(test6b)
train6b = CenterData(train6b)
test6c = CenterData(test6c)
train6c = CenterData(train6c)
test6d = CenterData(test6d)
train6d = CenterData(train6d)
test7b = CenterData(test7b)
train7b = CenterData(train7b)
train7c = CenterData(train7c)
test7c = CenterData(test7c)
train7d = CenterData(train7d)
test7d = CenterData(test7d)
test8b = CenterData(test8b)
train8b = CenterData(train8b)
test8c = CenterData(test8c)
train8c = CenterData(train8c)
train9b = CenterData(train9b)
test9b = CenterData(test9b)
train9c = CenterData(train9c)
test9c = CenterData(test9c)

trainX, trainy = ReshapeData(train0, train1, train2, train3, train4, train5, train6, train7, train8, train9, train0b,
                             train5b, train6b, train1b, train3b, train4b, train7b, train8b, train9b, train2b, train4c,
                             train7c, train9c, train6c, train7d, train8c, train6d)
testX, testy = ReshapeData(test0, test1, test2, test3, test4, test5, test6, test7, test8, test9, test0b, test5b, test6b,
                           test1b, test3b, test4b, test7b, test8b, test9b, test2b, test4c, test7c, test9c,
                           test6c, test7d, test8c, test6d)

knn.Use_K_Of(15)
knn.Fit(trainX, trainy)
predRight = 0
for row in range(0, 100):
    prediction = int(knn.Predict(testX[row, :]))
    actual = int(testy[row])
    if prediction == actual:
        predRight += 1
    else:
        print row
        print prediction, actual

percentage = predRight
# print testX
# print testy

print predRight
print percentage

pickle.dump(knn, open("classifier.p", "wb"))
