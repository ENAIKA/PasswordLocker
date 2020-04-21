#!/usr/bin/env python3.6
from user import User
from accounts import Credentials

def create_user(firstname,password):
    '''
    Function to create a new user
    '''
    new_user = User(firstname,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_users(firstname):
    '''
    Function that finds a user by firstname and returns the user
    '''
    return User.find_user(firstname)

def check_existing(firstname):
    '''
    Function that check if a user exists with the firstname and return a Boolean
    '''
    return User.user_exist(firstname)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

    #Credentials Class

def create_account(accountName,username,password):
    '''
    Function to create a new account
    '''
    new_account = Credentials(accountName,username,password)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()

def del_account(account):
    '''
    Function to delete account
    '''
    account.delete_account()

def find_account(accountName):
    '''
    Function that finds a user account by accountName and returns the account
    '''
    return Credentials.find_account(accountName)

def check_existing_account(accountName):
    '''
    Function that check if an account exists with the accountName and return a Boolean
    '''
    return Credentials.account_exist(accountName)

def display_account():
    '''
    Function that returns all user accounts
    '''
    return Credentials.display_accounts()

def copy_clipboard(accountName):
    '''
    Function that copies password to clipboard
    '''
    return Credentials.copy_password(accountName)

def gen_password(accountName):
    '''
    Function to generate passwords
    '''
    return Credentials.gen_password(accountName)

def main():
    print("Hello Welcome to passwordLocker What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
       

    while True:
        print("Use these short codes : cu - create a new user, du - display user, fu -find a user,l- login, ex -exit")

        short_code = input().lower()

        if short_code == 'cu':
            print("New User")
            print("-"*10)

            print ("First name ....")
            fname = input()

            print("Enter your password")
            pword = input()


            save_user(create_user(fname,pword)) # create and save new user.
            print ('\n')
            print(f"New User {fname} created successfully")
            print ('\n')

        elif short_code == 'du':

            if display_user():
                print("Here is a list of all users")
                print("\n")                    

                for user in display_user():
                    print(f"{user.firstname} \n")

                                    
            else:
                print('\n')
                print("No user with such a name\n")
                                
        elif short_code == 'fu':

            print("Enter the username you want to search")

            search_user = input()
            if check_existing(search_user):
                search_user = find_users(search_user)
                print(f"{search_user.firstname}")
                print('-' * 20)

            else:
                print("The user does not exist")
        elif short_code=="l":
            print("Enter username")
            username=input()
        
            print("Enter password")
            password = input()
                        
            if check_existing(username):
                if password==find_users(username).password:
                    print("Login was successful")
                    print('-' * 20)
                    
                else:
                    print("please check the password")

            while True:
                print("Use these short codes : ca - create new account credentials, da - display accounts, fa -find account,cp-copy account password,del-delete account, ex -exit")

                short_codes = input().lower()
                if short_codes == 'ca':
                    print("New Account Credentials")
                    print("-"*10)
                    
                    print ("Account name i.e facebook, twitter ....")
                    accountname = input()

                    print ("username ....")
                    username = input()

                    print("Enter your password")
                    pword = input()
                    if len(pword)==0:
                        password=gen_password(accountname)
                    else:
                        password=pword

                    save_account(create_account(accountname,username,password)) # create and save new account credential.
                    print ('\n')
                    print(f"New Account: {accountname} username:{username} password:{password} was created successfully")
                    print ('\n')

                elif short_codes == 'da':

                    if display_account():
                        print("Here is a list of all accounts")
                        print("\n")                    

                        for account in display_account():
                            print(f"{account.accountName} {account.username} {account.password}")
                            print ('\n')
                                    
                    else:
                        print('\n')
                        print("No account\n")

                elif short_codes == 'fa':

                    print("Enter the account name you want to search")

                    search_account = input()
                    if check_existing_account(search_account):
                        search_account = find_account(search_account)
                        print(f"{search_account.accountName} {search_account.username} {search_account.password}")
                        print('-' * 20)

                    else:
                        print("The account does not exist")
                elif short_codes == 'del':
                    print("The account will be deleted")
                    print("Account Name")
                    accountname=input()
                    if check_existing_account(accountname):
                        accountname = find_account(accountname)
                    
                        del_account((accountname)) #del account.
                        print ('\n')
                        print(f"Account {accountname.accountName} deleted successfully")
                    else:
                        print("The account does not exist")

                elif short_codes == 'cp':
                    print("The password will be copied to clipboard")
                    print("Account Name")
                    accountname=input()
                    if check_existing_account(accountname):
                        accountname = find_account(accountname)
                    
                        copy_clipboard(accountname.accountName) #copy password.
                        print ('\n')
                        print(f"Account {accountname.accountName}'s password: {accountname.password} copied to clipboard successfully")
                    else:
                        print("The account does not exist")

                elif short_codes == "ex":
                    print("Logging out.  Bye .......")
                    break
                else:
                    print("I really didn't get that. Please use the short codes")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that.Please use the short codes")

if __name__ == '__main__':

    main()