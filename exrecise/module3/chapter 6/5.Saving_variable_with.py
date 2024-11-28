student = [("Alice",22),("Bob",25),("Charlie",20)]

with open("student.txt","w") as file:
    for name,age in student:
        file.write("Name:{},Age:{}\n".format(student[0],student[1]))