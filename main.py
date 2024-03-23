from worker.lib import LibSortWorker
from worker.quicksort import QuickSortWorker
from common.common import *


def Main():
    # Init worker sorting array using library
    LibSortWorker(
        input_file_path=PATH_INPUT,
        output_file_path=PATH_OUTPUT_LIB_SORT,
    )
    
    # Init worker sorting array using quicksort algorithm
    QuickSortWorker(
        input_file_path=PATH_INPUT,
        output_file_path=PATH_OUTOUT_QUICK_SORT,
    )


if __name__ == "__main__":
    Main()
