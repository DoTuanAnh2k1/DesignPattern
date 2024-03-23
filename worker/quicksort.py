from helper.file import ReadFile, WriteFile
from helper.log import Log
from SortAlgo.quicksort import SortArray
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
    using quick sort algorithm.
"""
def QuickSortWorker(
        input_file_path: str,
        output_file_path: str,
):
    try:
        # Read the file from the input path.
        Log("Reading file from input file...")
        array = ReadFile(filepath=input_file_path)

        # Sorting the array.
        timeSortQuick = Timer()
        Log("Sorting array using quicksort algorithm...")
        timeSortQuick.start()
        SortArray(array)
        Log(f"Sorting array using quicksort algorithm complete, time: {timeSortQuick.stop()}")

        # Write the sorted array to the output file.
        Log("Writing sorted array to output file...")
        WriteFile(filepath=output_file_path, arr=array)
    except Exception as e:
        Log(f"Worker/lib error: {e}")
