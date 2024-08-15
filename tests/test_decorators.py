import pytest
from src.decorators import log, my_function



def test_log():
    @log()
    def add_numbers(a, b):
        return a + b

    result = add_numbers(3, 5)
    assert result == 8


def test_log_output(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "Function start working.\nFunction finish working.\n\n"

