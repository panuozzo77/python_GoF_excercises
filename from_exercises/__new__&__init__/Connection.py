"""
Creami una sorta di singleton che utilizzi __new__ in modo tale da controllare se una variabile protetta sia istanziata o meno. Se lo è dimmelo e restituiscila comunque
"""
class Connection:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None :
            print("Connecting...")
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print("WARNING: There's already a connection!")
            return cls.__instance

    def __init__(self):
        print("Connected")

connection = Connection()
connection2 = Connection()
print("are these 2 connections the same?: ", connection is connection2)

>>Connecting...
>>Connected
>>WARNING: There's already a connection!
>>Connected
>>are these 2 connections the same?:  True
