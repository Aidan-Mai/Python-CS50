from twttr import shorten

def main():
    test_upper_lower()
    test_numberic()
    test_symbol()

def test_upper_lower():
    assert shorten("twitter") == 'twttr'
    assert shorten("TWITTER") == 'TWTTR'
    assert shorten("TwIttER") == 'TwttR'
def test_numeric():
    assert shorten('12345') == '12345'
    assert shorten('-12345') == '-12345'
def test_symbol():
    assert shorten("tw!tt^&") == 'tw!tt^&'
    assert shorten('t*itte*') == 't*tt*'

if __name__ == "__main__":
    main()

