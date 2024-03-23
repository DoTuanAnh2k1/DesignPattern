import os
from helper.log import Log


"""
    Read the contents of a file and return them as a list of integers.

    Args:
        filepath (str): The path to the file to be read.

    Returns:
        list: A list containing the integers read from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
"""
def ReadFile(filepath: str) -> list:
    try:
        with open(filepath, 'r') as file:
            content = file.readlines()
            
        content = [int(line.strip()) for line in content]
        return content
    except FileNotFoundError:
        Log(f"File '{filepath}' not found.")
        return None
    except Exception as e:
        Log(f"Error reading file '{filepath}': {e}")
        return None


"""
    Write a list of integers to a file.

    Args:
        filepath (str): The path to the file to be written.
        arr (list[int]): The list of integers to be written to the file.
"""
def WriteFile(filepath: str, arr: list[int]):
    try:
        mode = 'w'  
        if os.path.exists(filepath):  
            mode = 'w'

        with open(filepath, mode) as file:
            for num in arr:
                file.write(f"{num}\n")
        
        Log(f"Array has been written to '{filepath}'.")
    except Exception as e:
        Log(f"Error writing file '{filepath}': {e}")
