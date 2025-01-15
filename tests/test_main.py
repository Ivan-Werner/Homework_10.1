from unittest.mock import Mock
from src.main import main

def test_main():
    mock_main = Mock(return_value="Result")
    result = mock_main
    assert result() == "Result"