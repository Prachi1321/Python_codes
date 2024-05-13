
dict2={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
n=int(input("enter"))
if n>=0:

    if n in dict2:
        a=dict2.get(n)
        print(a)


