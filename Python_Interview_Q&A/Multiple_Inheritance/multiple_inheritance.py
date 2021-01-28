class A: 

    def display(self):
        print("Print from Class A")
class B:

    def display(self):
        print("Print from Class B")

class C(A,B):
  
    def display(self):
        print("Print from Class C")

obj = C()
obj.display()
obj = B()
obj.display()
