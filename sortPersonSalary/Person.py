class Person:
    def __init__(self, name, address, salary):
        self.name = name
        self.address = address
        self.salary = salary


    def __repr__(self):
        return repr((self.name, self.address, self.salary))            


    def display(self):
        print('Name: ' + self.name)
        print('Address: ' + self.address)
        print('Salary: ' + self.salary)
