from basic_function import get_weather, add, divide
import pytest

def test_weather_hot():
    assert get_weather(20)=='hot', 'The temperature is colder'

def test_weather_cold():
    assert get_weather(10)=='cold', 'The temperature is colder'

def test_add():
    assert add(2,3) == 5, '2+3 should be 5'
    assert add(-1,1)==0, '-1+1 should be 0'
    assert add(0,0)==0, '0+0 should be 0'

def test_divide_failed():
    with pytest.raises(ValueError, match='Cannot divide by zero'):
        divide(10,0)

def test_divide_well():
    assert divide(10,1)==10, '10/1 should be 10'