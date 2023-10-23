class Vehicle:
    def __new__(cls, wheels : int):
        if wheels == 2:
            return Motorbike()
        elif wheels == 4:
            return Car()
        else:
            return super().__new__(cls)

    def __init__(self, wheels : int):
        self.wheels = wheels
        print(f'Initializing vehicle with {wheels} wheels')

class Motorbike:
    def __init__(self):
        print('Initializing Motorbike')

class Car:
    def __init__(self):
        print('Initializing Car')

mb = Vehicle(2)
print('\n')
bus = Vehicle(6)
print('\n')
car = Vehicle(4)

>>Initializing Motorbike
>>Initializing vehicle with 6 wheels
>>Initializing Car
