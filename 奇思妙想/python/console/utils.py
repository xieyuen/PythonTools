from hashlib import sha256 as _sha256


def sha256(data: str) -> str:
    """
    sha256 hash
    :param data:
    :return: hashlib.sha256(str.encode('utf-8')).hexdigest()
    """
    return _sha256(data.encode('utf-8')).hexdigest()
