import os
from src.utils import operations_data
from config import DATA_DIR


operations_path = os.path.join(DATA_DIR, "operations.json")
def test_operations_data_empty(operations_data_empty_fix):
    assert operations_data('') == operations_data_empty_fix
