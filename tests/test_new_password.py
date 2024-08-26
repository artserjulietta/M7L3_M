import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters
def test_password():
    p = generate_password(6)
    assert len(p) == 6

def test_password_2():
    p1 = generate_password(4)
    p2 = generate_password(4)
    assert p1 != p2