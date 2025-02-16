name="Agrima"
weight=40
age=12
student=True

print("Data type on name before type casting", type(name))
print("Data type on weight before type casting", type(weight))
print("Data type on age before type casting", type(age))
print("Data type on student before type casting", type(student))

weight=int(weight)
age=str(age)
student=str(student)

print("Data type on weight before type casting", type(weight))
print("Data type on age before type casting", type(age))
print("Data type on student before type casting", type(student))
