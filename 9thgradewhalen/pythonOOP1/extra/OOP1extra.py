import ast
import base64
import sys
import time
import json


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Customer(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.permissions = "Customer"
    def __str__(self):
        return f'Name: {self.name} ID: {self.id}'


class Employee(User):
    def __init__(self, id, name, job):
        super().__init__(id, name)
        self.job = job
        self.permissions = "Employee"
    def __str__(self):
        return f'Name: {self.name} ID: {self.id} Job: {self.job} Permissions: {self.permissions}'
    

class Manager(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.permissions = "Manager"
    def __str__(self):
        return f'Name: {self.name} ID: {self.id} Permissions: {self.permissions}'


userData = []
continueSigningIn = True


def managerPowers():
    outputUsers = input(f'Manager, do you want to see the users in the list? (y/n) ')
    if outputUsers.lower() == 'y':
        print(userData)
        endLoop = input(f'Manager, do you want to shut down and save the list in this sign in system? (y/n) ')
        if endLoop.lower() == 'y':
            global continueSigningIn
            continueSigningIn = False
            print('Shutting down...')
            with open('9thgradewhalen/pythonOOP1/extra/data.json', 'w') as data:
                data.write(json.dumps(userData, sort_keys = True, indent = 4))
            with open('9thgradewhalen/pythonOOP1/extra/encrypted.txt', 'w') as encrypted:
                strData = str(userData)
                encryptedData = base64.b64encode(strData.encode('utf-8'))
                encrypted.write(str(encryptedData.decode('utf-8')))
            time.sleep(2)

try:
    with open ('9thgradewhalen/pythonOOP1/extra/encrypted.txt', 'r') as file:
        data = file.read()
        byteData = data.encode('utf-8')
        global decryptedData
        partiallyDecrypted = base64.b64decode(byteData.decode('utf-8'))
        decryptedData = partiallyDecrypted.decode('utf-8')
        print(decryptedData)
        userData = userData + ast.literal_eval(decryptedData)
except FileNotFoundError: 
    pass

while continueSigningIn == True:
    logOption = input('Are you logging in or creating a user? (Login, Create)')
    if logOption.upper() in ('C', "CREATE"):
        print("Welcome to the check-in system for this business.")
        userType = input('What type of user are you? (Customer, Employee, or Manager) ')
        if userType.lower() == 'customer':
            nameInput = input('What is your name? ')
            passInput = input('Create a password: ')
            newCustomer = Customer(passInput, nameInput)
            print(f'Your name is {newCustomer.name}, and your unique Password is {newCustomer.id}. Thanks for signing in and remember to save your password! ')
            newCustomerDic = {
                'Name' : newCustomer.name,
                'Password' : newCustomer.id,
                'Permissions' : 'Customer'
            }
            userData.append(newCustomerDic)
        elif userType.lower() == 'employee':
            nameInput = input('What is your name? ')
            jobInput = input('What is your occupation? ')
            passInput = input('Create a password: ')
            newEmployee = Employee(passInput, nameInput, jobInput)
            print(f'Your name is {newEmployee.name}, and your unique Password is {newEmployee.id}. Your job is {newEmployee.job}. Thanks for signing in and remember to save your password! ')
            newEmployeeDic = {
                'Name' : newEmployee.name,
                'Password' : newEmployee.id,
                'Job' : newEmployee.job,
                'Permissions' : 'Employee'
            }
            userData.append(newEmployeeDic)
        elif userType.lower() == 'manager':
            nameInput = input('What is your name? ')
            passInput = input('Create a password: ')
            newManager = Manager(passInput, nameInput)
            print(f'Your name is {newManager.name}, and your unique Password is {newManager.id}. Thanks for signing in and remember to save your password! ')
            newManagerDic = {
                'Name' : newManager.name,
                'Password' : newManager.id,
                'Permissions' : 'Manager'
            }
            userData.append(newManagerDic)
            managerPowers()
        else:
            print('Please make sure you entered the correct user type.')
            time.sleep(1.5)
    elif logOption.upper() in ('L', 'LOGIN'):
        try:
            userNameInput = input('What user are you logging in as? ')
            for user in range(len(userData)):
                perms = userData[user]['Permissions']
                username = userData[user]['Name']
                password = userData[user]['Password']
                if username.lower() == userNameInput.lower():
                    passInput = input(f'What is you password, {username}?')
                    if passInput == password:
                        print(f'Thank you for signing in, {username}.')
                        if perms.lower() == 'manager':
                            managerPowers()
                    else: 
                        print('Your password is incorrect. Sorry!')
        except: 
            e = sys.exc_info()[1]
            print('Something went wrong, please try again!' + e.args[0])
            time.sleep(0.5)
    else:
        print('Something went wrong, try again!')
        time.sleep(0.5)