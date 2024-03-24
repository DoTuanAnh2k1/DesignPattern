# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 02:36:45 2024

@author: Admin
"""

import os
import datetime
from common.common import PATH_LOG


"""
    Log a string message to a specified log file.

    Args:
        log_string (str): The string message to be logged.
        log_path (str, optional): The path to the log file. Defaults to PATH_LOG.
"""
def Log(log_string: str, log_path: str = PATH_LOG):
    try:
        log_dir = os.path.dirname(log_path)
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(log_path, 'a') as log_file:
            log_file.write(f"[{current_time}] {log_string}\n")
        
        print(f"[LOGGER]: '{log_string}' to '{log_path}'")
    except Exception as e:
        print(f"[ERROR]: '{log_string}' to '{log_path}': {e}")
