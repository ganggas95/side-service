from hashlib import md5, sha256


def hashed_password(password: str) -> bytes:
    """
    Convert string password to hashed password base md5(sha256)
    @params password:str password
    @return hashed_password: str
    """
    return str(md5(
        str(sha256(
            str(password).encode("utf-8")
        ).hexdigest()).encode("utf-8")
    ).hexdigest()).encode("utf-8")
