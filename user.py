class User:
    """
    Class that generates new instances of users
    """
    users_list = [] # Empty contact list

    def __init__(self,firstname,password):
        self.firstname = firstname
        self.password = password

    def save_user(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        User.users_list.append(self)