from helper.log import Log

"""
    Sort a list of integers in ascending order.

    Args:
        arr (list): The list of integers to be sorted.

    Returns:
        list: The sorted list of integers.
"""
def SortArray(arr: list) -> list:
    try:
        arr.sort()
        return arr
    except Exception as e:
        Log(f"[ERROR] libsort module, err: {e}")
