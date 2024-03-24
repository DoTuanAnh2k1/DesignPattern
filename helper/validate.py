from common.common import PATH_OUTPUT_LIB_SORT
from helper.log import Log

def Validate():
    inputFilePaths = [
        PATH_OUTPUT_LIB_SORT,
    ]
    for inputFilePath in inputFilePaths:
        f = open(inputFilePath, "rt")
        FLAG = False
        tmp = 0
        i_str = f.readline()
        i = 0
        err_list = []
        Log(inputFilePath)
        while i_str:
            val = int(i_str)
            if val < tmp:
                FLAG = True
                err_list.append(i)
            tmp = val
            i_str = f.readline()
            i += 1
            if not i % 10000:
                Log(f"\033[K{i} errors={len(err_list)}\r", end="")
        if FLAG:
            Log(f"\nMr. Stalks, I don't feel so good: ({len(err_list)}) {err_list}")
            with open("./j12t_test_errors_result.txt", "wt") as f:
                f.write(f"{err_list}")
        else:
            Log("\nPhan dong vo cuc.")
