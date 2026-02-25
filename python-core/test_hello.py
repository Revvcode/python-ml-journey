from newhello import hello

def test_default():
    hello() == "hello, world"

def test_arguement():
    hello("David") == "hello, David"