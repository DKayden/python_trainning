
from operator import attrgetter, itemgetter
from pickle import TRUE
import Person


class PersonWrapper:
    p = Person

    def __init__(self,p):
        self.p = p


def checkInputString():
    while True:
        result = input()
        if not result:
            print('You must input string')
        else:
            return result


def checkInputSalary():
    while True:
        try:
            result = float(input())
            if result < 0:
                print('You must input salary greater than zero!!!')
            else:
                return result
        except ValueError:
            print('You must input digit.')
            print('Please input salary: ')


def checkInputInt():
    while True:
        try:
            result = int(input())
            if result <= 0:
                raise Exception("You must input number greater than zero!!!")
            return result
        except ValueError:
            print('Input must be digit.')


def checkInputNumber():
    print("Enter Number")
    number = checkInputInt()
    return number


def inputPersonInfo():
    Person = []
    print('Enter Name: ')
    name = checkInputString()
    Person.append(name)
    print('Enter Address: ')
    address = checkInputString()
    Person.append(address)
    print('Enter Salary: ')
    salary = checkInputSalary()
    Person.append(salary)
    return Person


def getSalary(Person):
    p = Person
    return p.salary

n = checkInputNumber()
# print(n)
# inputPersonInfo()
persons = []

for i in range(0,n):
    persons.append(inputPersonInfo())
print(persons)
print('Sorted person by salary:\n')
# persons.sort(key = getSalary)
sorted(persons, key=attrgetter('salary'),reverse=False)