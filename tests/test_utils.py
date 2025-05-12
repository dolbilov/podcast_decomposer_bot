import pytest

from podcast_decomposer_bot.utils import seconds_to_timestamp


@pytest.mark.parametrize(
    "seconds,expected",
    [
        (0, "00:00:00"),  # ровно 0
        (5, "00:00:05"),  # меньше минуты
        (65, "00:01:05"),  # чуть больше минуты
        (3599, "00:59:59"),  # за минуту до часа
        (3600, "01:00:00"),  # ровно час
        (3661, "01:01:01"),  # час и чуть больше
        (86399, "23:59:59"),  # за секунду до суток
    ],
)
def test_seconds_to_timestamp(seconds, expected):
    assert seconds_to_timestamp(seconds) == expected
