import unittest # Importing the unittest module
import pyperclip
from accounts import Credentials # Importing the Credentials class

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
        

    def test_save_account(self):
        '''
        test_save_account test case to test if the object is saved into
         the accounts list
        '''
        self.new_account.save_account() # saving new account
        self.assertEqual(len(Credentials.accounts_list),1)

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if multiple accounts
            can be saved
            '''
            self.new_account.save_account()
            test_account = Credentials("Instagram","Test","user123") # new account
            test_account.save_account()
            self.assertEqual(len(Credentials.accounts_list),2)
    
    def test_delete_account(self):
            '''
            test_delete_account to test if an account can be removed from list
            '''
            self.new_account.save_account()
            test_account = Credentials("Instagram","Test","user123") # new account
            test_account.save_account()

            self.new_account.delete_account()# Deleting account 
            self.assertEqual(len(Credentials.accounts_list),1)

    def test_find_account(self):
        '''
        test to check accounts by accountName and display information
        '''

        self.new_account.save_account()
        test_account = Credentials("Instagram","Test","user123") # new account
        test_account.save_account()

        found_account = Credentials.find_account("Instagram")

        self.assertEqual(found_account.password,test_account.password)

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find account.
        '''

        self.new_account.save_account()
        test_account = Credentials("Instagram","Test","user123") # new account
        test_account.save_account()

        account_exists = Credentials.account_exist("Instagram")

        self.assertTrue(account_exists)

    def test_display_accounts(self):
        '''
        method that returns a list of accounts saved
        '''

        self.assertEqual(Credentials.display_accounts(),Credentials.accounts_list)


    def test_copy_password(self):
        '''
        Test to copy password from a found account
        '''

        self.new_account.save_account()
        
        self.new_account.copy_password("Twitter")

        self.assertEqual(self.new_account.password, pyperclip.paste())

    def test_gen_password(self):
        '''
        Test to generate password for account
        '''
        
        account=Credentials.gen_password("Facebook")
        test_account=Credentials("Facebook","Nakish",account)
        test_account.save_account()
        test_account.password=Credentials.gen_password(test_account)
        

        self.assertEqual(test_account.password, account)

if __name__ == '__main__':
    unittest.main()