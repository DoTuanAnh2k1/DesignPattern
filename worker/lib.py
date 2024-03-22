"""
Created on Fri Mar 22 18:50:09 2024

@author: Admin
"""
from helper.file import ReadFile, WriteFile
from helper.log import Log
from SortAlgo.libsort import SortArray

def LibSortWorker(inputfilepath: str, outputfilepath: str):
    try:
        # Read file from file in input path
        Log("Read File from input file")
        array = ReadFile(filepath = inputfilepath)
        
        # Sorting
        Log("Sorting array")
        SortArray(array)
        
        # Write out put array after sorting 
        # to output file path
        Log("Write output array to output tile")
        WriteFile(filepath = outputfilepath, arr = array)
    except Exception as e:
        Log(f"Worker/lib, error: {e}")
        