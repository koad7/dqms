# DataQualityManagement/tests/test_calculator.py

from dqms.core.calculator import add

def test_add():
    assert add(2, 3) == 5
