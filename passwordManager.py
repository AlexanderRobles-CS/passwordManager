from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import base64

def loadKey():
    with open("key.key", "rb") as file:                                    # rb = read bytes
        key = file.read()
    return key

def deriveKey(key, masterPassword, salt):                                  # Derive key from master password
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    derivedKey = kdf.derive(key + masterPassword.encode())                 # Encode master password to bytes
    return derivedKey

def encryptPassword(password, key):                                        # Encrypt password
    encryptedPassword = key.encrypt(password.encode())
    return encryptedPassword.decode()

def decryptPassword(encryptedPassword, key):                               # Decrypt password
    decryptedPassword = key.decrypt(encryptedPassword.encode())
    return decryptedPassword.decode()

masterPassword = input("What is the master password? ")

key = loadKey()
salt = b'some_salt_value'

fernetKey = deriveKey(key, masterPassword, salt)                          # Derive key from master password
encodedKey = base64.urlsafe_b64encode(fernetKey)                          # Encode key to base64
fernetKey = Fernet(encodedKey)                                            # Create Fernet object

def viewPassword():
    with open("passwords.txt", "r") as f:                                 # r = read
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split(" | ")
            decryptedPassword = decryptPassword(password, fernetKey)
            print("User:", user, ", Password:", decryptedPassword)

def addPassword():                                                       # Add new password
    accountName = input("Account name: ")
    accountPassword = input("Password: ")
    encryptedPassword = encryptPassword(accountPassword, fernetKey)
    
    with open("passwords.txt", "a") as f:                                # a = append
        f.write(accountName + " | " + encryptedPassword + "\n")

while True:
    mode = input("Would you like to add a new password or view an existing one? (add/view), Press q to quit. ").lower()

    if mode == "q":
        break

    if mode == "add":
        addPassword()

    elif mode == "view":
        viewPassword()

    else:
        print("Invalid mode selected.")
        continue
