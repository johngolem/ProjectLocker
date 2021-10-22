# class credentials:
#   '''
#  class that holds credentials commands and functions

# '''
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
