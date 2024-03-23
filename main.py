from worker.lib import *
from common.common import *


def Main():
    # init worker sorting array using library
    LibSortWorker(
        input_file_path=PATH_INPUT,
        output_file_path=PATH_OUTPUT_LIB_SORT,
    )


if __name__ == "__main__":
    Main()
