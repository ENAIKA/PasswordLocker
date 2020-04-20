class Credentials:
    '''
    Class that generates new instances of Credentials
    '''
    accounts_list=[] #empty accounts list

    def __init__(self, accountName, username, password):
        self.accountName=accountName
        self.username=username
        self.password=password

    def save_account(self):

        '''
        save_account method saves Credentials objects into accounts_list
        '''

        Credentials.accounts_list.append(self)

    def delete_account(self):

        '''
        delete_account method deletes a saved account
        '''

        Credentials.accounts_list.remove(self)

    @classmethod
    def find_account(cls,accountName):
        '''
        Method that takes in account name and returns an account that matches the accountName.

        Args:
            accountName: name to be searched
        Returns :
           account that matches the accountName
        '''

        for account in cls.accounts_list:
            if account.accountName == accountName:
                return account

    @classmethod
    def account_exist(cls,accountName):
        '''
        Method that checks if an account exists from the accounts list.
        Args:
            accountName: name to be searched
        Returns :
            Boolean: dependent on the existance of the account
        '''
        for account in cls.accounts_list:
            if account.accountName == accountName:
                    return True

        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.accounts_list


    