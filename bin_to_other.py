'''This Is Program To Convert A Binary No To Other Numbering System'''
print("********** Various Numbering System *********")
bin_no=input("Enter Any Binary Number = ")
no=int(bin_no,2)
print(f"Given No {bin_no}'s Decimal Representation = {no}")
print(f"Given No {bin_no}'s Octal Representation = {oct(no)}")
print(f"Given No {bin_no}'s Hexadecimal Representation = {hex(no)}")