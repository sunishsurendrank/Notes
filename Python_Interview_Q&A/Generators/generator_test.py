import random

name = ["Sunish", "Sinoj", "Prasoon", "Sujith", "Jayesh"]
majors = ["Maths", "Biology", "Physics", "English", "Mechanical" ]

def studentgenerator(count):
    for i in range(count):
        person = {
                    'id': i,
                    'name': random.choice(name),
                    'major': random.choice(majors)
        }
        yield person

people = studentgenerator(10)
print(people)
for item in people:
    print(item)


