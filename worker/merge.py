from helper.file import ReadFile, WriteFile
from helper.log import Log
from SortAlgo.libsort import SortArray
from SortAlgo.mergesort import MergeSort
from model.timer import Timer

"""
- Input:
    + inputfilepath:  Path to the input number file.    - string
    + outputfilepath: Path to the output number file.   - string

- Output:
    + None.

- Summary:
    This function sorts an array from the file specified by inputfilepath
    and writes the sorted array to the file specified by outputfilepath
    using the library.
"""

def MergeSortWorker(
        input_file_path: str,
        output_file_path: str,        
):
    try:
        # Read the file from the input path.
        Log("Reading file from input file...")
        array = ReadFile(filepath=input_file_path)

        # Sorting the array.
        timeSortMerge = Timer()
        timeSortMerge.start()
        n = len(array)
        MergeSort(array,0,n-1)
        Log(f"Sorting array using mergesort complete, time: {timeSortMerge.stop()}")

        # Write the sorted array to the output file.
        Log("Writing sorted array to output file...")
        WriteFile(filepath=output_file_path, arr=array)        
    except Exception as e:
        Log(f"Worker/merge error: {e}")