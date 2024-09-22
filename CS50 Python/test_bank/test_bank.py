from bank import value

def main():
    test_zero()
    test_twenty()
    test_hundred()


def test_zero():
    assert value("hello, Aidan") == 0
    assert value ("HeLLo") == 0
    assert value ("Hello") == 0

def test_twenty():
    assert value ("Heck") == 20
    assert value("Hiya pals") == 20
def test_hundred():
    assert value ("give me that 100") == 100
    assert value ("good afternoon") == 100

if __name__ == "__main__":
    main()