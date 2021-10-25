import random
import string


class User:
    '''
    class that holds user functions.

    '''
    user_list = []  # empty users list

    def __init__(self, username, password):
        """
            init method that helps us define the properties of the user class

        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        Function that saves new user to the userlist array
        """
        User.user_list.append(self)

    @ classmethod
    def delete_user(self):
        User.user_list.remove(self)

    def displays_users(cls):
        return cls.user_list


class Credentials:
    '''
      class that holds credentials commands and functions
   '''

    credential_list = []

    def __init__(self, account, username, password):
        self.account = account
        self.username = username
        self.password -= password

    def delete_account(self):
        Credentials.credential_list.remove(self)

    def add_account(self):
        Credentials.credential_list.append(self)

    def ver_user(cls, username, password):
        a_user = " "
        for user in User.credential_list:
            if (user.username == username.credenatial_list and user.password == password):
                a_user == user.username
            return a_user

    @ classmethod
    def find_account(cls, account):
        for credential in cls.credential_list:
            if credential.account == account:
                return account

    @classmethod
    def find_account_exist(cls, account):
        for credential in cls.credential_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_accounts(cls):
        return cls.credential_list

    def generatePassword(stringLength=8):
        """Generate a random password string of letters and digits and special characters"""
        password = string.ascii_uppercase + \
            string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
