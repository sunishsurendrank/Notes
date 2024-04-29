
import random
import os
import psutil

name = ["Sunish", "Sinoj", "Prasoon", "Sujith", "Jayesh"]
majors = ["Maths", "Biology", "Physics", "English", "Mechanical" ]

"""
Generator have more benifits than List. Memory consumption when we use generators is low.

many programming languages have similar constructs to generators in Python. Some examples include:

Iterators in Java
Coroutines in Kotlin
Generators in JavaScript
Enumerators in Ruby
Generators in C#
These constructs allow for efficient and memory-friendly iteration in those programming languages.

For more info : https://youtu.be/bD05uGo_sVI
"""

def memory_usage_psutil():
    # return the memory usage in MB
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

def studentlist(count):
    result = []
    for i in range(count):
        person = {
                    'id': i,
                    'name': random.choice(name),
                    'major': random.choice(majors)
        }
        result.append(person)
    return result

def studentgenerator(count):
    for i in range(count):
        person = {
                    'id': i,
                    'name': random.choice(name),
                    'major': random.choice(majors)
        }
        yield person


print ('Memory (Before): {}Mb'.format(memory_usage_psutil()))

#people = studentlist(1000000)
people = studentgenerator(1000000)
print(people)
for item in people:
    print(item)

print ('Memory (After) : {}Mb'.format(memory_usage_psutil()))
