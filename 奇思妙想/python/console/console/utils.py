from hashlib import sha256 as _sha256, md5 as _md5


def md5(data: str | bytes) -> str:
    """
    md5 hash
    :param data:
    :return: hashlib.md5(data.encode('utf-8')).hexdigest()
    """
    if isinstance(data, bytes):
        return _md5(data).hexdigest()
    if isinstance(data, str):
        return _md5(data.encode('utf-8')).hexdigest()


def sha256(data: str | bytes) -> str:
    """
    sha256 hash
    :param data:
    :return: hashlib.sha256(data.encode('utf-8')).hexdigest()
    """
    if isinstance(data, bytes):
        return _sha256(data).hexdigest()
    if isinstance(data, str):
        return _sha256(data.encode('utf-8')).hexdigest()


def account2dict(data: list) -> dict:
    """
    list[Account] to dict
    :param data:
    :return:
    """
    pass
