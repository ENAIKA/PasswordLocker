import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.
    '''

    def setUp(self):
        '''
        Set up method runs before each test cases.
        '''
        self.new_user = User("Naika","Nakish254") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.firstname,"Naika")
        self.assertEqual(self.new_user.password,"Nakish254")

    def test_save_user(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_user.save_user() # saving the new contact
        self.assertEqual(len(User.users_list),1)

    
if __name__ == '__main__':
    unittest.main()