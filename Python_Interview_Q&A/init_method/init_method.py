class employee:

    def __init__(self,name="Sinoj",age="30"):
        self.name = name 
        self.age = age

    def display(self):
        print("Name:{0},Age:{1}".format(self.name,self.age))
    

obj = employee()
#---------------------------------------
obj1 = employee()
obj1.name = "Sunish"
obj1.age = "20"
#---------------------------------------
obj2 = employee("abc","12")
#---------------------------------------
obj.display()
obj1.display()
obj2.display()





