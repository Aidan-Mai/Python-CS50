import pytest
from fuel import convert, gauge


def main():
    test_correct()
    test_zero()
    test_string()
def test_correct():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("99/100") == 99 and gauge(99) == "F"
    assert convert("1/100") == 1 and gauge(1) == "E"
def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
def test_string():
    with pytest.raises(ValueError):
        convert("Mike/Jack")




if __name__ == "__main__":
    main()