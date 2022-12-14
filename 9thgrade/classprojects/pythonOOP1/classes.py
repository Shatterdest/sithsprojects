import uuid
import time


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

users = []
continueSigningIn = True
while continueSigningIn == True:
    print("Welcome to the check-in system for this business.")
    userType = input('What type of user are you? (Customer, Employee, or Manager) ')
    if userType.lower() == 'customer':
        nameInput = input('What is your name? ')
        newCustomer = Customer(uuid.uuid4(), nameInput)
        print(f'Your name is {newCustomer.name}, and your unique ID is {newCustomer.id}. Thanks for signing in! ')
        newCustomerDic = {
            'Name' : newCustomer.name,
            'ID' : newCustomer.id
        }
        users.append(newCustomerDic)
    elif userType.lower() == 'employee':
        nameInput = input('What is your name? ')
        jobInput = input('What is your occupation? ')
        newEmployee = Employee(uuid.uuid4(), nameInput, jobInput)
        print(f'Your name is {newEmployee.name}, and your unique ID is {newEmployee.id}. Your job is {newEmployee.job}. Thanks for signing in! ')
        newEmployeeDic = {
            'Name' : newEmployee.name,
            'ID' : newEmployee.id,
            'Job' : newEmployee.job,
            'Permissions' : 'Employee'
        }
        users.append(newEmployeeDic)
    elif userType.lower() == 'manager':
        nameInput = input('What is your name? ')
        newManager = Manager(uuid.uuid4(), nameInput)
        print(f'Your name is {newManager.name}, and your unique ID is {newManager.id}. Thanks for signing in! ')
        newManagerDic = {
            'Name' : newManager.name,
            'ID' : newManager.name,
            'Permissions' : 'Manager'
        }
        users.append(newManagerDic)
        outputUsers = input(f'Manager, do you want to see the users in the list? (y/n) ')
        if outputUsers.lower() == 'y':
            print(users)
            endLoop = input(f'Manager, do you want to shut down and clear the list in this sign in system? (y/n) ')
            if endLoop.lower() == 'y':
                continueSigningIn = False
                print('Shutting down...')
                time.sleep(2)
    else:
        print('Please make sure you entered the correct user type.')
        time.sleep(3)
