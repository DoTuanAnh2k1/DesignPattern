"""
Created on Fri Mar 22 18:50:09 2024

@author: Admin
"""
from helper.file import ReadFile, WriteFile
from SortAlgo.libsort import SortArray

def LibSortWorker(inputfilepath: str, outputfilepath: str):
    try:
        # Read file from file in input path
        array = ReadFile(inputfilepath)
        
        # Sorting
        SortArray(array)
        
        # Write out put array after sorting 
        # to output file path
        WriteFile(outputfilepath)
    except Exception as e:
        print("Worker/lib, error: ", e)
        