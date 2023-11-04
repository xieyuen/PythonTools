from hashlib import sha256 as __sha256, md5 as __md5


def md5(data: str | bytes, *, encode='utf-8') -> str:
    """
    md5 hash
    :param data:
    :param encode: str.encode(encode)
    :return: hashlib.md5(data.encode('utf-8')).hexdigest()
    """
    if isinstance(data, bytes):
        return __md5(data).hexdigest()
    if isinstance(data, str):
        return __md5(data.encode(encode)).hexdigest()


def sha256(data: str | bytes, *, encode='utf-8') -> str:
    """
    sha256 hash
    :param data:
    :param encode: str.encode(encode)
    :return: hashlib.sha256(data.encode('utf-8')).hexdigest()
    """
    if isinstance(data, bytes):
        return __sha256(data).hexdigest()
    if isinstance(data, str):
        return __sha256(data.encode(encode)).hexdigest()
