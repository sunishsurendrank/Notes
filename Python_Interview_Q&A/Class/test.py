class Calculate_and_Store:

    def __init__(self, __dbConnection):
        self.__dbConnection = __dbConnection
    
    def add (self, num1, num2):
        sum = num1 + num2
        print(f"Store {sum} using {self.__dbConnection} instance")


DBConnection    = "Connect"
cal             = Calculate_and_Store(DBConnection)
value           = cal.add(1,2)
value2          = cal.add(3,4)





