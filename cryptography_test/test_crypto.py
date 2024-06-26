import pytest

from cryptography.cryptography import *

def test_encrypt_shift_positive():
    # Test with positive shift value
    assert encrypt("abc", 1) == "bcd"
    assert encrypt("xyz", 3) == "abc"

def test_encrypt_shift_negative():
    # Test with negative shift value
    assert encrypt("bcd", -1) == "abc"

def test_encrypt_mixed_case():
    # Test with mixed case input
    assert encrypt("Hello World", 5) == "Mjqqt Btwqi"
    assert encrypt("Python", -2) == "Nwrfml"


def test_decrypt_shift_positive():
    # Test with positive shift value
    assert decrypt("bcd", 1) == "abc"
    assert decrypt("abc", 3) == "xyz"

def test_decrypt_shift_negative():
    # Test with negative shift value
    assert decrypt("abc", -1) == "bcd"

def test_decrypt_mixed_case():
    # Test with mixed case input
    assert decrypt("Mjqqt Btwqi", 5) == "Hello World"
    assert decrypt("Nwrfml", -2) == "Python"
