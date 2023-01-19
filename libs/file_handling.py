import os.path
def is_real_file(file:str):
    """
    Checks if a file exists
    
    PARAMS
    ------
    * file `str` the file to be checked
    """
    return os.path.isfile(file)