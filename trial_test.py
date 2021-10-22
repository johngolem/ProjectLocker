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


if __name__ == "__main__":
    unittest.main()
