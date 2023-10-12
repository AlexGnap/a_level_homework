import csv
from exceptions import EmailAlreadyExistsException


class Employee:
    def __init__(self, name, daily_salary, email):
        self.name = name
        self.daily_salary = daily_salary
        try:
            self.validate(email)
            self.email = email
        except EmailAlreadyExistsException as e:
            print(f'Error: {e} already exists')
            raise
        self.save_email()

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name} '

    def work(self):
        return 'I come to the office.'

    def check_salary(self, days):
        return self.daily_salary * days

    def validate(self, email):
        with open('emails.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for i in reader:
                if i in reader:
                    raise EmailAlreadyExistsException(f'{email} already exists')

    def save_email(self):
        with open('emails.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.email])

    def __lt__(self, other):
        return self.daily_salary < other.daily_salary

    def __le__(self, other):
        return self.daily_salary <= other.daily_salary

    def __eq__(self, other):
        return self.daily_salary == other.daily_salary

    def __ne__(self, other):
        return self.daily_salary != other.daily_salary

    def __gt__(self, other):
        return self.daily_salary > other.daily_salary

    def __ge__(self, other):
        return self.daily_salary >= other.daily_salary


class Recruiter(Employee):

    def get_position(self):
        return 'Recruiter'

    def __str__(self):
        return f'{self.get_position()} : {self.name}'

    def work(self):
        return 'I come to the office and start to hiring..'


class Developer(Employee):
    def __init__(self, name, daily_salary, email, tech_stack=None):
        super().__init__(name, daily_salary, email)
        self.tech_stack = tech_stack or []

    def get_position(self):
        return 'Developer'

    def __str__(self):
        return f'{self.get_position()} : {self.name}'

    def work(self):
        return 'I come to the office and start to coding..'

    def __add__(self, other):
        concat_name = self.name + ' ' + other.name
        comb_stack = list(set(self.tech_stack + other.tech_stack))
        salary = max(self.daily_salary, other.daily_salary)
        return concat_name, comb_stack, salary

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ne__(self, other):
        return len(self.tech_stack) != len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)


a = Employee('John', 25, 'john@gmail.com')
print(a.name)
print(a)

b = Recruiter('Klo', 45, 'email@ukr.net')
print(b)
c = Developer('New', 48, 'new@gmail.com', 'JS')
c1 = Developer('Jason', 48, 'superdev@gmail.com', ['Java', 'Ruby'])
print(c1)
c2 = Developer('Jules', 40, 'jb@yahoo.com', ['Python', 'Java', 'ASP.NET'])

print(a.work())
print(b.work())
print(b)
print(c)
print(c1)
print(b < c)
print(b <= c)
print(b == c)

print(c1 < c2)

print(b.check_salary(2))
print(c.check_salary(4))
print(c1.check_salary(7))

print(c1 + c2)

