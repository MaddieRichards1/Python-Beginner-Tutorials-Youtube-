
from cryptography.fernet import Fernet  #module which allows you to encrypt text


'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)''' #comment out once file created


# write_key() type this to create file

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)
# key + password + text to encrypt = random text
# random text + key + password = text to encrypt   # simplification of the module

def view():
    with open('passwords.txt', 'r') as f: #r is read file
        for line in f.readlines():
            data = line.rstrip()  #strips the /n of the line
            user, passw = data.split("|")   #removes | and put commas
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())



def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:   #with automatically closes the file, passwords.txt is the name of the file a is the mode adds a new file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")  #new line



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press Q to quit. ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue

