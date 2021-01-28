class parent:
    
    def __init__(self,parentname,parentage):
        self.parentname = parentname
        self.parentage = parentage

    def display(self):
        print("Parent Name: {0}, Parent Age: {1}".format(self.parentname,self.parentage))

class child(parent):

    def __init__(self,parentname,parentage,childschool):
        
        self.childschool = childschool
        super().__init__(parentname,parentage)

    def childdisplay(self):
        print("Parent Name: {0}, Parent Age: {1}, Child School: {2}".format(self.parentname,self.parentage,self.childschool))

obj = child("sinoj","30","ABC")

obj.childdisplay()
obj.display()