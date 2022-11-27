'''c_price=int(input("Enter Mobile Current Price : "))
c_coup=input("Enter Coupon Code : ")

def DisOffer():
    if c_coup.upper()=="HAPPY05":
        print(f"Mobile Current Price {c_coup}")
        print(f"Mobile Price After Discount Offer ") '''
import bz2
s = b'This is GFG author, and final year student.'
print(len(s))
  
# using bz2.compress(s) method
t1= bz2.compress(s)
print(len(t1))
# using bz2.decompress(s) method
t2 = bz2.decompress(t1)
print(len(t2))
