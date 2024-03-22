import os

def ReadFile(filepath: str) -> list:
    try:
        with open(filepath, 'r') as file:
            content = file.readlines()
            
        content = [int(line.strip()) for line in content]
        return content
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file '{filepath}': {e}")
        return None


def WriteFile(filepath: str, arr: list[int]):
    try:
        mode = 'w'  
        if os.path.exists(filepath):  
            print(f"File '{filepath}' already exists. Overwriting...")
            mode = 'w'

        with open(filepath, mode) as file:
            for num in arr:
                file.write(f"{num}\n")
        
        print(f"Array has been written to '{filepath}'.")
    except Exception as e:
        print(f"Error writing file '{filepath}': {e}")

