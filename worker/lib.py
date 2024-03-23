from helper.file import ReadFile, WriteFile
from helper.log import Log
from SortAlgo.libsort import SortArray


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
def LibSortWorker(inputfilepath: str, outputfilepath: str):
    try:
        # Read the file from the input path.
        Log("Reading file from input file...")
        array = ReadFile(filepath=inputfilepath)
        
        # Sorting the array.
        Log("Sorting array...")
        SortArray(array)
        
        # Write the sorted array to the output file.
        Log("Writing sorted array to output file...")
        WriteFile(filepath=outputfilepath, arr=array)
    except Exception as e:
        Log(f"Worker/lib error: {e}")
