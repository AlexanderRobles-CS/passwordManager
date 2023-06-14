from encryption import Encryption

class User:
    def viewPassword(self, encryption):

        with open("passwords.txt", "r") as f:                                                         # Read passwords.txt file

            for line in f.readlines():
                data = line.rstrip()
                decryptedData = encryption.decryptPassword(data, encryption.fernetKey)
                username, account_name, password = decryptedData.split(" | ")
                print("Account:", account_name, ", Username:", username, ", Password:", password)

    def addPassword(self, encryption):                                                       # Add new password
        account_name = input("Account name: ")
        username = input("Username: ")
        account_password = input("Password: ")
        
        encryptedData = encryption.encryptPassword(username + " | " + account_name + " | " + account_password, encryption.fernetKey)
        
        with open("passwords.txt", "a") as f:
            f.write(encryptedData + "\n")