absolute_path = r'D:\python\exrecise\module3\chapter 6\1.txt'
with open (absolute_path,'r') as file:
    content = file.read()
    print(content)

relative_path = '../1.txt'
with open (relative_path,'r') as file:
    content = file.read()
    print(content)