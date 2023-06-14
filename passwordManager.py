from encryption import Encryption
from user import User

if __name__ == "__main__":

    masterPassword = input("What is the master password? ")

    encryption = Encryption(masterPassword)
    encryption.deriveFernetKey(masterPassword)

    user = User()

    user.main(user, encryption)
