class Employee:
    def __init__(self, name, daily_salary):
        self.name = name
        self.daily_salary = daily_salary

    def work(self):
        return 'I come to the office.'

    def check_salary(self, days):
        return self.daily_salary * days

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
    def __init__(self, name, daily_salary, tech_stack=None):
        super().__init__(name, daily_salary)
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


a = Employee('John', 25)
print(a.name)

b = Recruiter('Klo', 45)
c = Developer('New', 48)
c1 = Developer('Jason', 48, ['Java', 'Ruby'])
c2 = Developer('Jules', 40, ['Python', 'Java', 'ASP.NET'])

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

