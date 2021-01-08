import uuid
import hashlib


def hash_password(password_str: str) -> str:
    """
    На вход получает строку пароль password_str
    И возвращает строку вида <хеш>:<соль>
    """
    # uuid используется для генерации случайного числа
    # 123
    # "123".encode() -> b"123" 00101101010111
    # UUID('6bd6c3cf-ff3a-41be-b573-5c8c732ad004')
    # '071b71c8db6a4a69a854bfc8d046cbfd'
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password_str.encode()).hexdigest() + ':' + salt


def check_password(hashed_password: str, user_password: str) -> bool:
    """
    Проверяет, что хеш от строки user_password соответствует хешу в hashed_password
    И возвращает равенство True/False
    """
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
