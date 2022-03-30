
from operator import itemgetter


def check_input_string():
    while True:
        result = input()
        if not result:
            print('You must input string')
        else:
            return result


def check_input_salary():
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


def check_input_int():
    while True:
        try:
            result = int(input())
            if result <= 0:
                raise Exception("You must input number greater than zero!!!")
            return result
        except ValueError:
            print('Input must be digit.')


def check_input_number():
    print("Enter Number")
    number = check_input_int()
    return number


def input_person_info():
    persons = []
    print('Enter Name: ')
    name = check_input_string()
    persons.append(name)
    print('Enter Address: ')
    address = check_input_string()
    persons.append(address)
    print('Enter Salary: ')
    salary = check_input_salary()
    persons.append(salary)
    return persons


n = check_input_number()
persons = []
for i in range (0,n):
    persons.append(input_person_info())

print('Before sort:')

print(persons)

print('Sorted person by salary:')

print(sorted(persons, key=itemgetter(2)))