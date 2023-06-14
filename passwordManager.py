from encryption import Encryption
from user import User

if __name__ == "__main__":

    masterPassword = input("What is the master password? ")

    encryption = Encryption(masterPassword)
    encryption.deriveFernetKey(masterPassword)

    user = User()

    while True:
        mode = input("Would you like to add a new password or view an existing one? (add/view), Press q to quit. ").lower()

        if mode == "q":
            break

        if mode == "add":
            user.addPassword(encryption)

        elif mode == "view":
            user.viewPassword(encryption)

        else:
            print("Invalid mode selected.")
            continue
