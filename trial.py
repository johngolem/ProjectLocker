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

    @classmethod
    def find_account(cls, account):
        for credential in cls.credential_list:
            if credential.account == account:
                return account

    def find_account_exist(cls, account):
        for credential in cls.credential_list:
            if credential.account == account:
                return True
        return False


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

    @classmethod
    def delete_user(self):
        User.user_list.remove(self)

    def displays_users(cls):
        return cls.user_list
