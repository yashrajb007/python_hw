"""Program For Encoding And Decoding Of String In Python"""
import bz2
from Color_Console import color
color(text="Yellow",bg="blue")
_abc=bz2.compress(b'I Am Learning Python 3')

print("\n******* Before Encoding *******\n")
print(_abc)
_pqr=bz2.decompress(_abc)
print("\n******* After Decoding *******\n")
print(_pqr)


