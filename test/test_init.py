import code.main as main


def testSadCase():
    assert not main.inc(3) == 5


def testHappyCase():
    assert main.inc(4) == 5
