"""Program For Error Handlers In Python"""
from Color_Console import color
color(text="Yellow",bg="blue")
_mystring="It’s a great first language because Python code is concise and easy to read."
_mystring1="Its a great first language because Python code is concise and easy to read."
print(" This Is Real String ".center(108,'*'))
print("\n*",_mystring,"\n")
print(" This Is Encoded String ".center(108,'*'))
print("\n*",_mystring.encode("ascii", errors="namereplace"))
print("\n*",_mystring.encode("ascii", errors="replace"))
print("\n*",_mystring.encode("ascii", errors="xmlcharrefreplace"))
print("\n*",_mystring1.encode("ascii", errors="strict"),"\n")
print("\n*",_mystring.encode("ascii", errors="strict"))