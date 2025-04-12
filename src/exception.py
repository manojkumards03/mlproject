import sys
import os
from datetime import datetime
from src.logger import logging
def error_message_detail(error, detail):
    """
    Print the error message with details.
    """
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno 
    print(f"Error occurred in file: {file_name}, line: {line_number}, error: {error}, detail: {detail}")


class CustomException(Exception):
    """
    Custom exception class to handle exceptions in the project.
    """
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
