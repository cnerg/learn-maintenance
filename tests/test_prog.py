from src.prog_package import prog

def test_unitToInch():
    assert 10 == prog.unitToInch("in", 10)
    assert 2 == prog.unitToInch("in", 2)
    assert 36 == prog.unitToInch("ft", 3)
    assert 84 == prog.unitToInch("ft", 7)
    assert 36 == prog.unitToInch("yd", 1)
    assert 72 == prog.unitToInch("yd", 2)
    assert 126720 == prog.unitToInch("mi", 2)
    assert 316800 == prog.unitToInch("mi", 5)
    assert 4 == round(prog.unitToInch("cm", 10.16))
    assert 6 == round(prog.unitToInch("cm", 15.24))
    assert 200 == round(prog.unitToInch("m", 5.08))
    assert 152 == round(prog.unitToInch("m", 3.8608))
    assert 96542301 == round(prog.unitToInch("km", 2452.174445))
    assert 21671 == round(prog.unitToInch("km", 0.5504434))

def test_inchToUnit():
    assert 10 == prog.inchToUnit("in", 10)
    assert 2 == prog.inchToUnit("in", 2)
    assert 3 == prog.inchToUnit("ft", 36)
    assert 7 == prog.inchToUnit("ft", 84)
    assert 1 == prog.inchToUnit("yd", 36)
    assert 2 == prog.inchToUnit("yd", 72)
    assert 2 == prog.inchToUnit("mi", 126720)
    assert 5 == prog.inchToUnit("mi", 316800)
    assert 10.16 == round(prog.inchToUnit("cm", 4), 2)
    assert 15.24 == round(prog.inchToUnit("cm", 6), 2)
    assert 5.08 == round(prog.inchToUnit("m", 200), 2)
    assert 3.8608 == round(prog.inchToUnit("m", 152), 4)
    assert 2452.174445 == round(prog.inchToUnit("km", 96542301), 6)
    assert 0.5504434 == round(prog.inchToUnit("km", 21671), 7)

def test_crossProduct():
    array = prog.crossProduct([2,-1,3,3,2,1])
    assert (array[0] == -7) & (array[1] == 7) & (array[2] == 7) & (len(array) == 3)
    array = prog.crossProduct([6,0,-3,0,6,0])
    assert (array[0] == 18) & (array[1] == 0) & (array[2] == 36) & (len(array) == 3)  
    
