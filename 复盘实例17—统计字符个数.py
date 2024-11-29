import string
letter=0
digit=0
space=0
other=0
zeta=input("请输入你的字符串：")
for i in zeta:
    if i.isalpha():
        letter+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        digit+=1
    else:
        other+=1
print(letter,digit,space,other)