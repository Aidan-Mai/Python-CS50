from um import count
import pytest

def main():
    test_noums()
    test_ums()
    test_punctiation()


def test_noums():
    assert count("yummy") == 0
    assert count("thisdoesnotcountasum") == 0
def test_ums():
    assert count("um") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um") == 2

def test_punctiation():
    assert count("um?") == 1

if __name__ == "__main__":
    main()
