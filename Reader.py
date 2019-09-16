import pickle
class READER:
    def __init__(self):
        pickle_in = open("userData/gesture1.p", "rb")
        gestureData = pickle.load(pickle_in)
        print gestureData