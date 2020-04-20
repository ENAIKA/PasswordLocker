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

    