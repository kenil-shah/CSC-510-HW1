import code as cd


def testSadCase():
    assert not cd.inc(3) == 5


def testHappyCase():
    assert cd.inc(4) == 5
