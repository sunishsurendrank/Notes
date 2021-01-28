
file = open("D:\\GitHub\Python\\Interview Questions\\Comprehension\\test.txt","r")
#print(len(file.read().split()))

print(len( [word for word in file.read().split() if word != "are"] ))