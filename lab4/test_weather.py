from pytest_mock import MockerFixture

import weather_lib
from main import main

def test(mocker: MockerFixture):
    mocker.patch('weather_lib.get_weather_info_text', return_value = "test")
    assert weather_lib.get_weather_info_text() == "test"