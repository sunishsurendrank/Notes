import argparse #library



Parseobject = argparse.ArgumentParser()

Parseobject.add_argument("Name",type=str)
Parseobject.add_argument("Age",type=int)

arguments = Parseobject.parse_args()

print(arguments)


