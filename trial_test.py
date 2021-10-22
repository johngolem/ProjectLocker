import unittest
from trial import User


class TestUser(unittest.TestCase):
    '''
    class that defines the test cases for the user class.
    '''

    def setUp(self):
        """
       setup method to run before each test case. .
        """
        self.new_user = User("Johnpaul", "qwerty123@")  # create User object

    def test_init_(self):
        '''
        testing if object has been correctly initialized
        '''
        self.assertEqual(self.new_user.username, "Johnpaul")
        self.assertEqual(self.new_user.password, "qwerty123@")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def save_multiple_users(self):
        self.new_user.save_user()
        test_user = User("Testuser", "passtest123$")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


if __name__ == "__main__":
    unittest.main()
