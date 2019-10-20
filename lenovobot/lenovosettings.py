from cryptography.fernet import Fernet
from sms import send

key = b'VRYVm3P5pRgUVwTF2dt5T4oHpBdMW78k3E0kibU8BNY='
cipher_suite = Fernet(key)

usersettings = open("user.txt", "r")
data = usersettings.readlines()

with open('user.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line


def setup(answer12):
    if answer12 == 0:
        print("Welcome to the Lenovo Bot. Please complete the setup.")
        changeroasd = input("New phone number (xxxxxxxxxx): ") + "\n"
        with open('user.txt', 'w') as file:
            file.write(changeroasd)
        carrier123 = input("Carrier (verizon, sprint, tmobile, att): ") + "\n"
        with open('user.txt', 'a') as file:
            file.write(carrier123)

        send("Successfully changed phone number")
        print("Successfully changed phone number. If you don't recieve a text please make sure you put in the "
              "right phone number. ")
        logemails = input("New login email: ") + "\n"
        with open('user.txt', 'a') as file:
            file.write(logemails)
        input_pass = input("New login password: ")
        ciphered_pass = cipher_suite.encrypt(input_pass.encode())
        with open('user.bin', 'wb') as file_object:
            file_object.write(ciphered_pass)
        while True:
            try:
                savedmin12 = input("New min saved price: ") + "\n"
                int(savedmin12)
                with open('user.txt', 'a') as file:
                    file.write(savedmin12)
                    break
            except:
                print("Please enter a number")
        while True:
            try:
                maxbuypricce = input("New max buy price: ") + "\n"
                int(maxbuypricce)
                with open('user.txt', 'a') as file:
                    file.write(maxbuypricce)
                    break
            except:
                print("Please enter a number")
        while True:
            try:
                maxbuypriccesare = input("New minimum percentage off of original price: ") + "\n"
                maxbuypricce12 = maxbuypriccesare.replace('%', '')
                with open('user.txt', 'a') as file:
                    file.write(maxbuypricce12)
                    break
            except:
                print("Please enter a percent")

        changelink = input("Do you want to narrow results? If so, type in link of narrowed results, otherwise "
                           "type 'n': ")
        if changelink != 'n':
            changeroo = changelink + '\n'
            with open('user.txt', 'a') as file:
                file.write(changeroo)
        else:
            coolchangeroo = 'https://www.lenovo.com/us/en/outletus/laptops/c/LAPTOPS?IPromoID=LEN251549'
            with open('user.txt', 'a') as file:
                file.write(coolchangeroo)
    if answer12 == 1:
        fawe = input("New phone number (xxxxxxxxxx): ") + "\n"
        with open('user.txt', 'w') as file:
            file.write(fawe)
        carrier123 = input("Carrier (verizon, sprint, tmobile, att): ") + "\n"
        with open('user.txt', 'a') as file:
            file.write(carrier123)
    if answer12 == 2:
        logemails = input("New login email: ") + "\n"
        with open('user.txt', 'a') as file:
            file.write(logemails)
        input_pass = input("New login password: ")
        ciphered_pass = cipher_suite.encrypt(input_pass.encode())
        with open('user.bin', 'wb') as file_object:
            file_object.write(ciphered_pass)
    if answer12 == 3:
        while True:
            try:
                savedmin12 = input("New min saved price: ") + "\n"
                int(savedmin12)
                with open('user.txt', 'a') as file:
                    file.write(savedmin12)
                    break
            except:
                print("Please enter a number")
        while True:
            try:
                maxbuypricce = input("New max buy price: ") + "\n"
                int(maxbuypricce)
                with open('user.txt', 'a') as file:
                    file.write(maxbuypricce)
                    break
            except:
                print("Please enter a number")
        while True:
            try:
                maxbuypriccesare = input("New minimum percentage off of original price: ") + "\n"
                maxbuypricce12 = maxbuypriccesare.replace('%', '')
                with open('user.txt', 'a') as file:
                    file.write(maxbuypricce12)
                    break
            except:
                print("Please enter a percent")
        changelink = input("Do you want to narrow results? If so, type in link of narrowed results, otherwise "
                           "type 'n': ")
        if changelink != 'n':
            changeroo = changelink + '\n'
            with open('user.txt', 'a') as file:
                file.write(changeroo)
        else:
            coolchangeroo = 'https://www.lenovo.com/us/en/outletus/laptops/c/LAPTOPS?IPromoID=LEN251549'
            with open('user.txt', 'a') as file:
                file.write(coolchangeroo)


def settingscool(errorsets):
    while True:
        answer1 = errorsets
        if answer1 == 0:
            print("\nHere is a list of all setting commands:")
            print("    - change phone number")
            print("    - change login credentials")
            print("    - change search parameters")
            print("    - done")
            answer = input("")
        else:
            answer = answer1
        if answer == "change phone number":
            data[0] = input("New phone number (xxxxxxxxxx): ") + "\n"
            with open('user.txt', 'w') as file:
                file.writelines(data)
            data[1] = input("Carrier (verizon, sprint, tmobile, att): ") + "\n"
            with open('user.txt', 'w') as file:
                file.writelines(data)
            send("Successfully changed phone number")
            print("Successfully changed phone number. If you don't recieve a text please make sure you put in the "
                  "right phone number. ")
        elif answer == "change login credentials":
            data[2] = input("New login email: ") + "\n"
            with open('user.txt', 'w') as file:
                file.writelines(data)
            input_pass = input("New login password: ")
            ciphered_pass = cipher_suite.encrypt(input_pass.encode())
            with open('user.bin', 'wb') as file_object:
                file_object.write(ciphered_pass)

        elif answer == "change search parameters":
            while True:
                try:
                    data[3] = input("New min saved price: ") + "\n"
                    int(data[3])
                    with open('user.txt', 'w') as file:
                        file.writelines(data)
                        break
                except:
                    print("Please enter a number")
            while True:
                try:
                    data[4] = input("New max buy price: ") + "\n"
                    int(data[4])
                    with open('user.txt', 'w') as file:
                        file.writelines(data)
                        break
                except:
                    print("Please enter a number")
            while True:
                try:
                    maxbuypriccesareas = input("New minimum percentage off of original price: ") + "\n"
                    data[6] = maxbuypriccesareas.replace('%', '')
                    with open('user.txt', 'w') as file:
                        file.writelines(data)
                        break
                except:
                    print("Please enter a percent")
            changelink = input("Do you want to narrow results? If so, type in link of narrowed results, otherwise "
                               "type 'n': ")
            if changelink != 'n':
                data[5] = changelink + '\n'
                with open('user.txt', 'w') as file:
                    file.writelines(data)

        elif answer == "done":
            break
        else:
            print("Invalid input")
