class Calculate_and_Store:

    def __init__(self, _dbConnection, num1, num2):
        self._dbConnection = _dbConnection
        self.num1           = num1
        self.num2           = num2
    
    def add (self):
        sum = self.num1 + self.num2
        print(f"Store {sum} using {self._dbConnection} instance")


DBConnection    = "Connect"
cal             = Calculate_and_Store(DBConnection,1,2)
value           = cal.add()
cal2            = Calculate_and_Store(DBConnection,3,4)
value2          = cal2.add()



