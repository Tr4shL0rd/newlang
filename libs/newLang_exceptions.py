class NL_FunctionNotFound(Exception):
    """
    Raised when a function isn't found
    
    PARAMS
    ------
    * functions_name `str` the name of the function that was not found
    * line_number `str|int` the line where the error happened 
    * file_name `str`  the name of the file where the error happened
    """
    def __init__(self, function_name:str, line_number:str|int, file_name:str):
        #__message = f"Function \"{function_name}\" was not found "
        __message = f"\"{function_name}\" was called but not found.  FILE {file_name}:{line_number}"
        super().__init__(__message)
        
class NL_InvalidLine(Exception):
    """
    Raised when a function isn't found
    
    PARAMS
    ------
    * line `str` the name of the function that was not found
    * line_number `str|int` the line where the error happened 
    * file_name `str`  the name of the file where the error happened
    """
    def __init__(self, line:str, line_number:str|int, file_name:str):
        #__message = f"Function \"{function_name}\" was not found "
        __message = f"\"{line}\" is invalid.  FILE {file_name}:{line_number}"
        super().__init__(__message)
