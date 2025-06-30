import pytest
import string
from password_generator import generate_password, validate_length

def test_generate_password_length():
    """Test if generated password has the correct length."""
    password = generate_password(length=10)
    assert len(password) == 10

def test_generate_password_contains_digits():
    """Test if password includes digits when requested."""
    password = generate_password(use_digits=True)
    assert any(c.isdigit() for c in password)

def test_generate_password_contains_symbols():
    """Test if password includes symbols when requested."""
    password = generate_password(use_symbols=True)
    assert any(c in string.punctuation for c in password)

def test_validate_length():
    """Test if length validation works correctly."""
    assert validate_length(8) is True
    assert validate_length(64) is True
    assert validate_length(7) is False
    assert validate_length(65) is False
pytest.main(["-v", "--tb=line", "-rN", __file__])