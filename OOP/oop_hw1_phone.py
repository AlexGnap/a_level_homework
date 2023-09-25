import csv


class Phone:
    phone_number = None
    _counter = 0

    def set_phone_number(self, number):
        self.phone_number = number

    def get_incoming_counter(self):
        return self._counter

    def get_call(self):
        self._counter += 1
        self.get_logging()

    def get_logging(self):
        with open("calls.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.phone_number, "Received"])


obj1 = Phone()
obj2 = Phone()
obj3 = Phone()

obj1.set_phone_number(4565676)
obj2.set_phone_number('380956363')
obj3.set_phone_number('98546363')
print(obj1.phone_number)
print(obj2.phone_number)
print(obj3.phone_number)

obj3.get_call()
obj3.get_call()
obj3.get_call()
obj1.get_call()
obj1.get_call()
obj2.get_call()
print(obj1.get_incoming_counter())
print(obj2.get_incoming_counter())
print(obj3.get_incoming_counter())


def get_total_incoming(phones):
    total = 0
    for phone in phones:
        total += phone.get_incoming_counter()
    return total


lst = [obj1, obj3, obj2]
print(get_total_incoming(lst))
