def is_comment(string:str) -> bool:
    """
    checks if string is a comment by seeing if either //, # or ; is in the line

    PARAMS
    ------
    * string `str` the line containing the possible comment
    """
    comment_tokens = ["//", "#", ";"]
    for token in comment_tokens:
        if string.startswith(token):
            return True
    return False
        #return True if string.startswith(token) else False  