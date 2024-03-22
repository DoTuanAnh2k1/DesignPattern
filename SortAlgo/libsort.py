def SortArray(arr: list) -> list:
    try:
        arr.sort()
        return arr
    except Exception as e:
        print("libsort module, err: ", e)