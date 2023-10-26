from pathlib import Path
import sys
from utils import read_file, sha256_encrypt

# Current dir path
DIR_PATH = str(Path(Path(__file__).parent.absolute()))
sys.path.insert(0, DIR_PATH)

# To test different passwords just create a .txt file and change PASSWORD_PATH
PASSWORD_PATH = DIR_PATH+"/data/password_wrong.txt"
PASSWORD_HASH_PATH = DIR_PATH+"/data/password_hash.txt" 


# Check if user password hash is the same as the hash file
def login():
    password = read_file(PASSWORD_PATH)
    # Show password to user
    print(f"The password in the file is: {password}")

    true_hash = read_file(PASSWORD_HASH_PATH)
    password_hash = sha256_encrypt(password)

    return password_hash == true_hash

def main() -> None:
    login_status = login()

    if login_status:
        print("Logged successfully!")
    else:
        print("Wrong password, try again.")


if __name__ == "__main__":
    main()