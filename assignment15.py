"""Program For Currency Conversion From Rupees To AUD,USD & EUR"""
import sys
from Color_Console import color
color(text="Blue",bg="white")

try : 
    while(True):
        print("    Currency Conversion From Indian Rupee    ".center(100,'⦾'),"\n")
        print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+- List Of Currency -+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-".center(100,'+') )
        print("\n\t\t1] USD [United States Doller]")
        print("\t\t2] AUD [Austrelian Doller]")
        print("\t\t3] EURO ")
        print("\t\t4] Exit")


        choice=int(input("\n\t\t◙ Enter Your Choice [1,2,3,4] = "))
        print()

        rupee=int(input("Enter A Amount In Rupee ₹ :"))
        if choice in [1,2,3,4]:
            if choice == 1:
                print(" Rupee ₹ To USD $(United States Doller) Conversion".center(100,'⦾'))
                print("\n\t\t① 81.72₹ = 1$ USD")
                print(f"\n\t\t① {rupee}₹ = {rupee/81.72}$")
                print('')
                a=input("\n\t\tDo You Want Continue [YES/NO] :")
                if a.upper()=='YES':
                    continue
                else:
                    print("\n\t\t # Thanks For Using This Program !")
                    sys.exit()

            elif choice == 2:
                print(" Rupee₹ To AUD $(Austrelian Doller) Conversion".center(100,'⦾'))
                print("\n\t\t① 53.98₹ = 1$ AUD")
                print(f"\n\t\t① {rupee}₹ = {rupee/53.98}$")
                print('')
                a=input("\n\t\tDo You Want Continue [YES/NO] :")
                if a.upper()=='YES':
                    continue
                else:
                    print("\n\t\tThanks For Using This Program !")
                    sys.exit()
            elif choice == 3:
                print(" Rupee ₹ To EURO € Conversion".center(100,'⦾'))
                print("\n\t\t① 83.70₹ = 1€ EURO")
                
                print(f"\n\t\t① {rupee}₹ = {rupee/83.70}€")
                print('')
                a=input("\n\t\tDo You Want Continue [YES/NO] :")
                if a.upper()=='YES':
                    continue
                else:
                    print("\n\t\tThanks For Using This Program !")
                    sys.exit()
            elif choice == 4:
                
                sys.exit()
        else:
            print("\n\t\t➤ Enter Valid Choice[1,2,3,4,5]")

except BaseException as ex:
    print(ex)
