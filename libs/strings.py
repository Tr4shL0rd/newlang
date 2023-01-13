def is_comment(string:str) -> bool:
    comment_tokens = ["//", "#", ";"]
    for token in comment_tokens:
        return True if string.startswith(token) else False  