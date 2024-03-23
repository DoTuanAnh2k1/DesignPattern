from worker.lib import *
from common.common import *

def Main():
    
    # init worker sorting array using library
    LibSortWorker(
        inputfilepath = PATH_INPUT,
        outputfilepath = PATH_OUTPUT_LIB_SORT,
    )

if __name__ == "__main__":
    Main()
