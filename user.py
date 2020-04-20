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
    
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the users_list
        '''

        User.users_list.remove(self)

    @classmethod
    def find_user(cls,firstname):
        '''
        Method that takes in firstname and returns a user that matches the firstname.

        Args:
            firstname: name to be searched
        Returns :
           user that matches the firstname
        '''

        for user in cls.users_list:
            if user.firstname == firstname:
                return user

    @classmethod
    def user_exist(cls,firstname):
        '''
        Method that checks if a user exists from the users list.
        Args:
            firstname: name to e searched
        Returns :
            Boolean: dependent on the existance of the user
        '''
        for user in cls.users_list:
            if user.firstname == firstname:
                    return True

        return False