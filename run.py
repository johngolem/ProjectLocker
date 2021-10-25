from trial import Credentials, User


def create_user(username, password):
    new_user = User(username, password)
    return new_user


def save_user():
    User.save_user


def display_user():
    User.displays_users


def login_user(username, password):
    check_user = Credentials.ver_user(username, password)
    return check_user


def create_new_credential(account, username, password):
    new_credential = Credentials.add_account(username, password)
    return new_credential


def save_credentials():
    Credentials.save_details()


def display_account_details():
    return Credentials.display_accounts


def delete_credential(Credentials):
    Credentials.delete_account()


def find_credential(account):
    return Credentials.find_account(account)


def check_credential(Credentials):
    return Credentials.find_account_exist()


def generate_password():
    auto_password = Credentials.generatePassword
    return auto_password


def password_locker():
    print("Hello User, Welcome to Password Locker..\n Type one of the following commands to proceed...\n CNA.. \n HA..\n ")
    short_code = input("").lower().strip()
    if short_code == "cna":
        print("Create New Account/Sign up")
        print('*' * 50)  # not understood!!!!!!!!!
        username = input("Username: ")
        while True:
            print("TP-type own password..\n GRP- generate random password")
            password_choice = input.lower().strip()
            if password_choice == "tp":
                password = input("Enter password: \n")
                break
            elif password_choice == "grp":
                password = generate_password()
            else:
                print("Invalid password please try again")
        save_user(create_user(username, password))
        print("*"*85)
        print(
            f"Hello:{username}, your account has been succesfully created! \n your password is: {password}")
        print("*"*85)
    elif short_code == "ha":
        print("*"*50)
        print("Enter your User name and your Password to log in:")
        print('*' * 50)
        username = input("Username: ")
        password = input("password: ")
        login = login_user(username, password)
        if login == login:
            print(f"Hello {username}.Welcome To PassWord Locker")
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create new Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(
                    " TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(
                account, userName, password))
            print('\n')
            print(
                f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_account_details():
                print("Here's your list of acoounts: ")

                print('*' * 30)
                print('_' * 30)
                for account in display_account_details():
                    print(
                        f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_' * 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(
                    f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(
                    f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print(
                    "That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_password()
            print(
                f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print(
                "Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print("Please enter a valid input to continue")


if __name__ == '__main__':
    password_locker()
