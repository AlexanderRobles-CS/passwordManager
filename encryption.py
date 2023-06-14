from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

import os
import base64

class Encryption:
    def __init__(self, masterPassword):
        self.key = self.loadKey()
        self.salt = b'some_salt_value'
        self.fernetKey = self.deriveFernetKey(masterPassword)
        self.derivedKey = self.deriveKey(self.key, masterPassword, self.salt)

    def generateKey(self):
        self.key = Fernet.generate_key()
        with open("key.key", "wb") as file:
            file.write(self.key)

    def loadKey(self):
        if not os.path.isfile("key.key"):
            self.generateKey()

        with open("key.key", "rb") as file:
            key = file.read()

        return key

    def deriveKey(self, key, masterPassword, salt):                                 # Derive key from master password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        derivedKey = kdf.derive(key + masterPassword.encode())                       # Encode master password to bytes
        return derivedKey

    def encryptPassword(self, password, key):                                        # Encrypt password
        encryptedPassword = key.encrypt(password.encode())
        return encryptedPassword.decode()

    def decryptPassword(self, encryptedPassword, key):                               # Decrypt password
        decryptedPassword = key.decrypt(encryptedPassword.encode())
        return decryptedPassword.decode()
    
    def deriveFernetKey(self, masterPassword):
        salt = b'some_salt_value'

        fernetKey = self.deriveKey(self.key, masterPassword, salt)                          # Derive key from master password
        encodedKey = base64.urlsafe_b64encode(fernetKey)                                    # Encode key to base64
        fernetKey = Fernet(encodedKey)                                                      # Create Fernet object

        return fernetKey