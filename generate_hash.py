# This code must be ran if password_correct is changed to update the hash

from pathlib import Path
import sys
from utils import read_file, write_file, sha256_encrypt

# Current dir path
DIR_PATH = str(Path(Path(__file__).parent.absolute()))
sys.path.insert(0, DIR_PATH)

PASSWORD_PATH = DIR_PATH+"/data/password_correct.txt"
PASSWORD_HASH_PATH = DIR_PATH+"/data/password_hash.txt"


# Create hash file from password file
def get_hash_file_from_pass() -> None:
    password = read_file(PASSWORD_PATH)
    password_hash = sha256_encrypt(password)
    write_file(PASSWORD_HASH_PATH, password_hash)


if __name__ == "__main__":
    get_hash_file_from_pass()
