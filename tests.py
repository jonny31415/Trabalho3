from login import login
from pathlib import Path
import sys
import pytest

# Current dir path
DIR_PATH = str(Path(Path(__file__).parent.absolute()))
sys.path.insert(0, DIR_PATH)

# To test different passwords just create a .txt file
PASSWORD_WRONG_PATH = DIR_PATH+"/data/password_wrong.txt"
PASSWORD_CORRECT_PATH = DIR_PATH+"/data/password_correct.txt"
PASSWORD_HASH_PATH = DIR_PATH+"/data/password_hash.txt"


# Execute tests with pytest
@pytest.mark.parametrize("password_path, expected", [(PASSWORD_WRONG_PATH, False),\
                                                     (PASSWORD_CORRECT_PATH, True)])
def test_login(password_path, expected):
    assert login(password_path) == expected
