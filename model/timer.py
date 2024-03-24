import time


# Timer for calculate time running sort algo
class Timer:
    def __init__(self):
        self.__time = None

    # Setting start of time
    def start(self):
        self.__time = time.time()

    # Setting time stop
    def stop(self):
        runningTime = time.time() - self.__time
        return runningTime
