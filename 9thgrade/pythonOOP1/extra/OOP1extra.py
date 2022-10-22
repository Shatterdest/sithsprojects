import ast
import base64
import uuid
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
usernames = []
def sortUserNames():
    for name in range(len(userData)):
        usernames.append(userData[name]['Name'])
        print(usernames)

def managerPowers():
    outputUsers = input(f'Manager, do you want to see the users in the list? (y/n) ')
    if outputUsers.lower() == 'y':
        print(userData)
        endLoop = input(f'Manager, do you want to shut down and save the list in this sign in system? (y/n) ')
        if endLoop.lower() == 'y':
            global continueSigningIn
            continueSigningIn = False
            print('Shutting down...')
            with open('9thgrade/pythonOOP1/extra/data.json', 'w') as data:
                data.write(json.dumps(userData, sort_keys = True, indent = 4))
            with open('9thgrade/pythonOOP1/extra/encrypted.txt', 'w') as encrypted:
                strData = str(userData)
                encryptedData = base64.b64encode(strData.encode('utf-8'))
                encrypted.write(str(encryptedData.decode('utf-8')))
            time.sleep(2)

try:
    with open ('9thgrade/pythonOOP1/extra/encrypted.txt', 'r') as file:
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
    logOption = input('Are you logging in or creating a user? (L, C)')
    if logOption.upper() == 'C':
        print("Welcome to the check-in system for this business.")
        userType = input('What type of user are you? (Customer, Employee, or Manager) ')
        if userType.lower() == 'customer':
            nameInput = input('What is your name? ')
            newCustomer = Customer(str(uuid.uuid4()), nameInput)
            print(f'Your name is {newCustomer.name}, and your unique Password is {newCustomer.id}. Thanks for signing in! ')
            newCustomerDic = {
                'Name' : newCustomer.name,
                'Password' : newCustomer.id
            }
            userData.append(newCustomerDic)
        elif userType.lower() == 'employee':
            nameInput = input('What is your name? ')
            jobInput = input('What is your occupation? ')
            newEmployee = Employee(str(uuid.uuid4()), nameInput, jobInput)
            print(f'Your name is {newEmployee.name}, and your unique Password is {newEmployee.id}. Your job is {newEmployee.job}. Thanks for signing in! ')
            newEmployeeDic = {
                'Name' : newEmployee.name,
                'Password' : newEmployee.id,
                'Job' : newEmployee.job,
                'Permissions' : 'Employee'
            }
            userData.append(newEmployeeDic)
        elif userType.lower() == 'manager':
            nameInput = input('What is your name? ')
            newManager = Manager(str(uuid.uuid4()), nameInput)
            print(f'Your name is {newManager.name}, and your unique Password is {newManager.id}. Thanks for signing in! ')
            newManagerDic = {
                'Name' : newManager.name,
                'Password' : newManager.id,
                'Permissions' : 'Manager'
            }
            userData.append(newManagerDic)
        else:
            print('Please make sure you entered the correct user type.')
            time.sleep(1.5)
    else:
        sortUserNames()
        print(usernames)
        userNameInput = input('What user are you logging in as? ')
        for name in usernames:
            password = userData[name]['Password']
            if name == userNameInput:
                passInput = input(f'What is you password, {name}?')
                if passInput == password:
                    
                    pass
