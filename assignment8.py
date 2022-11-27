"""Program For Write Different Examples Of Built In String Functions Of Python"""
from Color_Console import color
color(text="Yellow",bg="blue")
#We have to use built in function of python in that 5 strings 
a="Hello World...!"
b="This is Python 3,I am learning python programming "
c="Python is a high-level, general-purpose programming language"
d="It’s a great first language because Python code is concise and easy to read."
e="Its design philosophy emphasizes code readability with the use of significant indentation"


"""Capitalize() Function"""

print(" Examples Of capitalize() Functions ".center(108,'*'))
print("\n*",a.capitalize())
print("\n*",b.capitalize())
print("\n*",c.capitalize())
print("\n*",d.capitalize())
print("\n*",e.capitalize(),"\n")

"""Casefold() Function"""

print(" Examples Of casefold() Functions ".center(108,'*'))
print("\n*",a.casefold())
print("\n*",b.casefold())
print("\n*",c.casefold())
print("\n*",d.casefold())
print("\n*",e.casefold(),"\n")


"""center() Function"""

print(" Examples Of casefold() Functions ".center(108,'*'))
print("\n*",a.center(50,"+"))
print("\n*",b.center(100))
print("\n*",c.center(150,'A'))
print("\n*",d.center(1000))
print("\n*",e.center(10,"@"),"\n")



"""Endswith() Function"""

print(" Examples Of Endswith() Functions ".center(108,'*'))
print("\n*",a.endswith("!"))
print("\n*",b.endswith("Programming"))
print("\n*",c.endswith("age"))
print("\n*",d.endswith(" read"))
print("\n*",e.endswith("."),"\n")

"""Expandtabs() Function"""

a1="Hello\tWorld...!"
b1="This is Python 3,\tI am learning python programming "
c1="Python\tis\ta\thigh-level,\tgeneral-purpose\tprogramming\tlanguage"
d1="It’s\ta great first language because\tPython code is concise and easy to read."
e1="Its design philosophy emphasizes\tcode\treadability\twith the use of significant indentation"

print(" Examples Of Expandtabs() Functions ".center(108,'*'))
print("\n*",a1.expandtabs(10))
print("\n*",b1.expandtabs(2))
print("\n*",c1.expandtabs())
print("\n*",d1.expandtabs(5))
print("\n*",e1.expandtabs(1),"\n")


"""find() Functiom"""

print(" Examples Of find() Functions ".center(108,'*'))
print("\n*",a.find("l"))
print("\n*",b.find("in"))
print("\n*",c.find("-p"))
print("\n*",d.find("a",21))
print("\n*",e.find("it's",10),"\n") 

"""replace() Functiom"""

print(" Examples Of replace() Functions ".center(108,'*'))
print("\n*",a.replace("W","w"))
print("\n*",b.replace("3","2"))
print("\n*",c.replace("high-l","High-L"))
print("\n*",d.replace("read","learn"))
print("\n*",e.replace("I","i"),"\n") 

"""swapcase() Functiom"""

print(" Examples Of swapcase() Functions ".center(108,'*'))
print("\n*",a.swapcase())
print("\n*",b.swapcase())
print("\n*",c.swapcase())
print("\n*",d.swapcase())
print("\n*",e.swapcase(),"\n") 