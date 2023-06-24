def validate_user(username, minlen):
    assert type(username) == str, "username debe ser una cadena de texto"
    if minlen < 1:
        raise ValueError("minlen debe ser al menos 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True
