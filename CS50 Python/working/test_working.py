from working import convert
import pytest

def main():
    test_time()
    test_minute()
    test_format()
    test_hour()


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:00 PM to 8:00 AM") == "22:00 to 08:00"

def test_minute():
    with pytest.raises(ValueError):
        convert('9:60 AM to 9:60 PM')

def test_format():
    with pytest.raises(ValueError):
        convert('9 AM - 9 PM')

def test_hour():
    with pytest.raises(ValueError):
        convert('13 AM to 17 PM')

if __name__ == "__main__":
    main()
