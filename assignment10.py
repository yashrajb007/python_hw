"""Program For Showing name,value,type,requirement of bytes,address,length,hash value of list in Python"""
from Color_Console import color
color(text="Yellow",bg="blue")
numbers=["one","two","three",4,5,6,7,8,9,10]
print(" Actual List ".center(108,'*'))
print(numbers)
print(" Showing Information Of List ".center(108,'*'))
print("\n*",numbers)
print("\n*",type(numbers))
print(f"\n*"" Name Of Variable = numbers")
print(f"\n*"" Value Of Variable ={numbers}")
print(f"\n*"" Data Type Of Variable={type(numbers)}")
print(f"\n*"" Variable city requires={numbers.__sizeof__} bytes")
print(f"* Address Of Variable={id(numbers)}")
print(f"* length of numbers= {len(numbers)}")
print(f"* hash value of numbers= {hash(numbers)}")