from helper.log import Log


"""
    The partition function divides the array into two parts,
    such that elements smaller than the pivot are moved to 
    the left side of the pivot and elements greater than the 
    pivot are moved to the right side of the pivot.
    
    Parameters:
        arr (list): The array to be sorted.
        low (int): The index of the first element of the array.
        high (int): The index of the last element of the array.
        
    Returns:
        int: The index of the pivot after sorting.
"""
def partition(arr: list[int], low: int, high: int) -> int:    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

"""
    The quickSort function sorts the array arr using the Quick Sort algorithm.

    Parameters:
        arr (list): The array to be sorted.
        low (int): The index of the first element of the array.
        high (int): The index of the last element of the array.
"""
def quickSort(arr: list[int], low: int, high: int):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

"""
    The SortArray function uses the Quick Sort algorithm to sort the array arr.
    
    Parameters:
        arr (list): The array to be sorted.
"""
def SortArray(arr: list[int]):
    try:
        n = len(arr)
        quickSort(arr, 0, n - 1)
    except Exception as e:
        Log(f"[ERROR] SortAlgo/quicksort.py error: {e}")
