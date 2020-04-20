import unittest # Importing the unittest module
from accounts import Credentials # Importing the accounts class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the Credentials class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Credentials("Twitter","Muriuki","Muri5678") # create Credentials object
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.accounts_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.accountName,"Twitter")
        self.assertEqual(self.new_account.username,"Muriuki")
        self.assertEqual(self.new_account.password,"Muri5678")
        


if __name__ == '__main__':
    unittest.main()