"""Program For get choice from user end and calculate area of given space using conditional statement """
import sys
import math as a
from Color_Console import color
color(text="Blue",bg="white")

try : 
    while(True):
        print("    Calculate Area Of Space    ".center(100,'⦾'),"\n")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- List Of Space -+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-".center(100,'+') )
        print("\n\t\t1] Triangle")
        print("\t\t2] Circle")
        print("\t\t3] Square")
        print("\t\t4] Rectangle")
        print("\t\t5] Exit")


        choice=int(input("\n\t\t◙ Enter Your Choice [1,2,3,4,5] = "))
        print()


        if choice in [1,2,3,4,5]:
            if choice == 1:
                print(" Area Of Triangle ".center(100,'⦾'))
                base=float(input("\n\t\t◙ Enter The Base Of Triangle = "))
                height=float(input("\n\t\t◙ Enter The Height Of Triangle = "))
                area_of_triangle=1/2*base*height
                print("\n\t\t① Area Of Triangle = ",area_of_triangle)
                a=input("Do You Want Continue [YES/NO] :")
                if a.upper()=='YES':
                    continue
                else:
                    print("Thanks For Using This Program !")
                    sys.exit()

            elif choice == 2:
                print(" Area Of Circle ".center(100,'⦾'))
                radius=float(input("\n\t\t◙ Enter The Radius Of Circle = "))
                area_of_cicle = a.pi*radius**2
                print("\n\t\t① Area Of Circle = ",area_of_cicle)
                a=input("Do You Want Continue [YES/NO] :")
                if a.upper()=='YES':
                    continue
                else:
                    print("Thanks For Using This Program !")
                    sys.exit()
            elif choice == 3:
                print(" Area Of Square ".center(100,'⦾'))
                side=float(input("\n\t\t◙ Enter The Side Of Square = "))
                area_of_square = side**2 
                print("\n\t\t① Area Of Square = ",area_of_square)
                a=input("Do You Want Continue [YES/NO] :")
                if a.upper()=='YES':
                    continue
                else:
                    print("Thanks For Using This Program !")
                    sys.exit()
            elif choice == 4:
                print(" Area Of Rectangle ".center(100,'⦾'))
                width=float(input("\n\t\t◙ Enter The Width Of Rectangle = "))
                height=float(input("\n\t\t◙ Enter The Height Of Rectangle = "))
                area_of_rectangle=width*height
                print("\n\t\t① Area Of Rectangle = ",area_of_rectangle)
                a=input("Do You Want Continue [YES/NO] :")
                if a.upper()=='YES':
                    continue
                else:
                    print("Thanks For Using This Program !")
                    sys.exit()
            elif choice == 5:
                
                sys.exit()
        else:
            print("\n\t\t➤ Enter Valid Choice[1,2,3,4,5]")

except BaseException as ex:
    print(ex)
