from basic_pytest import get_weather

def test_weather_hot():
    assert get_weather(20)=='hot', 'The temperature is colder'

def test_weather_cold():
    assert get_weather(20)=='cold', 'The temperature is colder'