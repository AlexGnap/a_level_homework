# Зробити можливим порівнювати Employee по рівню ЗП.


class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return 'I come to the office.'

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

    def get_position(self):
        return 'Developer'

    def __str__(self):
        return f'{self.get_position()} : {self.name}'

    def work(self):
        return 'I come to the office and start to coding..'


a = Employee('John', 25)
print(a.name)

b = Recruiter('Klo', 45)
c = Developer('New', 48)

print(a.work())
print(b.work())
print(b)
print(c)
print(b < c)
print(b <= c)
print(b == c)
