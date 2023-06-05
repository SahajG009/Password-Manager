# real build
# advance password manager
# using symmetric encryption

from cryptography.fernet import Fernet

#generating the key
#no need for key generation as we have it
'''def gen_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as kf:
        kf.write(key)'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",fer.decrypt(passw.encode()).decode())

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



with open("master_password","r") as f:
    mst_pwd = f.readline()
if len(mst_pwd) != 0: 
    entr_pwd = input("Enter the Master Password: ")
    print(mst_pwd)
    print(fer.decrypt(mst_pwd.encode()).decode())
    if entr_pwd == (fer.decrypt(mst_pwd.encode()).decode()):
        print("Correct Password")
        while True:
            mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
            if mode == "q":
                break
            elif mode == "view":
                view()
            elif mode == "add":
                add()
            else:
                print("Invalid Mode.")
                continue
else:
    mst_file = open("master_password","w")
    pwd = input("Set Master Password: ")
    mst_file.write(fer.encrypt(pwd.encode()).decode())


