import socket


class sunish:
    def test(self,name,age):
        print(f"hello {name} {age}")


f_name = "Python_Interview_Q&A/Files and Folders/files_folders.py"
fileObject = open(f_name, "r")
fileObject1 = open(f_name, "r")
print(type(fileObject))
print(dir(fileObject))
print(id(fileObject))
print(callable(fileObject))
print("The file descriptor for %s is %s" % (f_name, fileObject.fileno()))
print("The file descriptor for %s is %s" % (f_name, fileObject1.fileno()))

fileObject.fileno()
object1 = sunish()
a = "sunish"
print(dir(object1))

