from cryptography.fernet import Fernet

masterPassword = input("What is the master password? ")

def viewPassword():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split(" | ")
            print("User: ", user, ", Password: ", password)

def addPassword():
    accountName = input("Account name: ")
    accountPassword = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(accountName + " | " + accountPassword + "\n")

while True:
    mode = input("Would you like to add a new password or view an existing one? (add/view), Press q to quit. ").lower()

    if mode == "q":
        break

    if mode == "add":
        addPassword()p

    elif mode == "view":
        viewPassword()

    else:
        print("Invalid mode selected.")
        continue

