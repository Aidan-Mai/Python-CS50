from plates import is_valid

def main():
    test_numbered()
    test_length_max_min()
    test_symbol()
    test_middle_number()
    test_two()

def test_numbered():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
def test_middle_number():
    assert is_valid("AB45B") == False
    assert is_valid("AAA222") == True
def test_length_max_min():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("GGHBHDMKB") == False
def test_two():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
def test_symbol():
    assert is_valid("PI3.14") == False
    assert is_valid("PI3!14") == False
    assert is_valid("PI 14") == False

if __name__ == "__main__":
    main()