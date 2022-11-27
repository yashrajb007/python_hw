'''This Is Program To Convert A Octal No To Other Numbering System'''
print("********** Various Numbering System *********")
oct_no=input("Enter Any Octal Number = ")
no=int(oct_no,8)
print(f"Given No {oct_no}'s Decimal Representation = {no}")
print(f"Given No {oct_no}'s Binary Representation = {bin(no)}")
print(f"Given No {oct_no}'s Hexadecimal Representation = {hex(no)}")