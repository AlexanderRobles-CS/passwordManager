import re
import os
from encryption import Encryption

class User:
    def viewPassword(self, encryption):

        while True:

            userInput = input("Do you want to view all passwords or a specific one? (all/one), press q to exit.  ").lower()

            if userInput == "q":
                break

            if userInput == "all":
                with open("passwords.txt", "r") as f:                                                         # Read passwords.txt file
                    
                    print("\n")
                    for line in f.readlines():
                        data = line.rstrip()
                        decryptedData = encryption.decryptPassword(data, encryption.fernetKey)
                        username, account_name, password = decryptedData.split(" | ")
                        print("Account:", account_name, ", Username:", username, ", Password:", password)
                    
                    print("\n")

            elif userInput == "one":
                searchConent = input("Enter the content to search: ")
                fileName = "passwords.txt"
                print("\n")
                if os.path.isfile(fileName):
                    with open(fileName, 'r') as file:
                        for line in file:
                            data = line.rstrip()
                            decryptedData = encryption.decryptPassword(data, encryption.fernetKey)
                            
                            if re.search(searchConent, decryptedData):
                                username, account_name, password = decryptedData.split(" | ")
                                print("Account:", account_name, ", Username:", username, ", Password:", password)
                                print("\n")
                                break
                        else:
                            print(f"Content '{searchConent}' not found in file '{fileName}'")
                else:
                    print(f"File '{fileName}' not found")
            else:
                print("Invalid mode selected.")


    def addPassword(self, encryption):                                                       # Add new password
        account_name = input("Account name: ")
        username = input("Username: ")
        account_password = input("Password: ")
        
        encryptedData = encryption.encryptPassword(username + " | " + account_name + " | " + account_password, encryption.fernetKey)
        
        with open("passwords.txt", "a") as f:
            f.write(encryptedData + "\n")

    def main(self, user, encryption):
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