import pickle
import os


class READER:
    def __init__(self):
        self.numGestures = 0
        pass
        # pickle_in = open("userData/gesture.p", "rb")
        # gestureData = pickle.load(pickle_in)
        # print gestureData

        def Read_Gesture(self, files):
            path, dirs, files = next(os.walk('userData'))
            self.numGestures = len(files)
            print files, dirs, path

    def Print_Gestures(self):
        for i in range(0, self.numGestures - 1):
            self.Read_Gesture()
