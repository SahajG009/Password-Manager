#basic password manager

master_pwd="master"

def add():
    acc = input("Account Name: ")
    acc_pwd = input("Account Password: ")

    with open('passwords.txt','a') as f:
        f.write("Account Name:" + acc + "\n" + "Account Password:" + acc_pwd + "\n")

def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            print(data)


def mode():
    while True:
        print("\n\tMode Selection")
        print("1. add - to add a new password")
        print("2. view - to view existing passwords")
        print("3. quit - to quit")
        mode_sel = input("Select the mode: ")
        if mode_sel == "add":
            add()
        elif mode_sel == "view":
            view()
        else:
            quit()

mstr_pwd = input("Master Password: ")

if mstr_pwd.lower() == master_pwd:
    print("The password is correct\n")
    mode()
else:
    pass

