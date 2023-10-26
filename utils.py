import hashlib

# Read content from file
def read_file(path: str) -> str:
    with open(path, "r") as f:
        content = f.readline()
    return content

# Write content to file
def write_file(path: str, content: str) -> None:
    with open(path, "w") as f:
        f.write(content)


# SHA256 encrypt password
def sha256_encrypt(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest() 