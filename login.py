from pathlib import Path
import sys
from utils import read_file, sha256_encrypt

# Current dir path
DIR_PATH = str(Path(Path(__file__).parent.absolute()))
sys.path.insert(0, DIR_PATH)

PASSWORD_HASH_PATH = DIR_PATH+"/data/password_hash.txt"


# Check if user password hash is the same as the hash file
def login(password_path):
    password = read_file(password_path)
    # Show password to user
    print(f"The password in the file is: {password}")

    true_hash = read_file(PASSWORD_HASH_PATH)
    password_hash = sha256_encrypt(password)

    return password_hash == true_hash
