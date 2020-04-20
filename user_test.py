import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.
    '''

    def setUp(self):
        '''
        Set up method runs before each test cases.
        '''
        self.new_user = User("Naika","Nakish254") # create contact object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.users_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.firstname,"Naika")
        self.assertEqual(self.new_user.password,"Nakish254")

    def test_save_user(self):
        '''
        test_save_contact test case to test if the user object is saved into
         the users list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.users_list),1)

    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple users
            users_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user123") # new user
            test_user.save_user()
            self.assertEqual(len(User.users_list),2)
    
    def test_delete_user(self):
            '''
            test_delete_user to test if a user can be removed from users list
            '''
            self.new_user.save_user()
            test_user = User("Test","user123") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting user object
            self.assertEqual(len(User.users_list),1)

    def test_find_user(self):
        '''
        test to check users by firstname and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user123") # new user
        test_user.save_user()

        found_user = User.find_user("Test")

        self.assertEqual(found_user.firstname,test_user.firstname)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("Test","user123") # new user
        test_user.save_user()

        user_exists = User.user_exist("Test")

        self.assertTrue(user_exists)


    
if __name__ == '__main__':
    unittest.main()