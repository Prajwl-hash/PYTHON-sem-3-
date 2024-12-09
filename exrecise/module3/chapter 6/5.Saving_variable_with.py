<<<<<<< HEAD
student = [("Alice",22),("Bob",25),("Charlie",20)]

with open("student.txt","w") as file:
    for name,age in student:
=======
student = [("Alice",22),("Bob",25),("Charlie",20)]

with open("student.txt","w") as file:
    for name,age in student:
>>>>>>> c965dbf5152de176c2dbd9448cc71dbd01538425
        file.write("Name:{},Age:{}\n".format(student[0],student[1]))