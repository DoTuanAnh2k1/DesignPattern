from worker.lib import *
from common.common import *

def Main():
    LibSortWorker(
        inputfilepath = PATH_INPUT,
        outputfilepath = PATH_OUTPUT,
        )
    pass

if __name__ == "__main__":
    Main()