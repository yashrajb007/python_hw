'''This Is Program To Convert A Hexadecimal No To Other Numbering System'''
print("********** Various Numbering System *********")
hex_no=input("Enter Any Hexadecimal Number = ")
no=int(hex_no,16)
print(f"Given No {hex_no}'s Decimal Representation = {no}")
print(f"Given No {hex_no}'s Binary Representation = {bin(no)}")
print(f"Given No {hex_no}'s Octal Representation = {oct(no)}")
