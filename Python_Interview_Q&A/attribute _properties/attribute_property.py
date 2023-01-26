class Misc1():
        def __init__(self):
            self.test = self.test_func()

        def test_func(self):
            print ('func running')
            return 'func value'
class Misc():

    @property
    def test(self):
        print ('func running')
        return 'func value'

print("-------attiibute-----")
c2 = Misc()
print (c2.test)
print (c2.test)

print("-------property-----")
cl = Misc()
print (cl.test)
print (cl.test)