from helper.log import Log
"""
    The mergeSort function sorts the array arr using the merge Sort algorithm.

    Parameters:
        arr (list): The array to be sorted.
"""

def mergeSort(arr: list) -> list:
    #Divided the array into 2 halves
    if len(arr) > 1:    
        leftArr = arr[:len(arr) // 2]
        rightArr = arr[len(arr) // 2:]

        #Recursion sort each half
        mergeSort(leftArr)
        mergeSort(rightArr)

        #Merge the sorted halves
        left_index, right_index, merged_index = 0, 0, 0
        while left_index < len(leftArr) and right_index < len(rightArr):
            if leftArr[left_index] < rightArr[right_index]:
                arr[merged_index] = leftArr[left_index]
                left_index += 1
            else:
                arr[merged_index] = rightArr[right_index]
                right_index += 1
            merged_index += 1

        #if rightArr is empty
        while left_index < len(leftArr):
            arr[merged_index] = leftArr[left_index]
            left_index += 1
            merged_index += 1


        #if leftArr is empty
        while right_index < len(rightArr):
            arr[merged_index] = rightArr[right_index]
            right_index += 1
            merged_index += 1

