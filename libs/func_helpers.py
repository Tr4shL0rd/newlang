def get_value(function:str) -> str:
    """
    Gets the value of a function by splitting at opening and closing parentheses

    PARAMS
    ------
    * function `str` the function that you need the value of
    """
    return function.split("(")[1].split(")")[0]