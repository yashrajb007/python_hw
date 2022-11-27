from Color_Console import color
color(text="Yellow",bg="blue")


print(" \tOur Service Is Only In This Location's\t ".center(85,'*'))
print("    Swargate, Hadapsar, Kothrud    ".center(85,'⦾'),"\n")
pick_up=input("\t◙ Pick Up Location : ")
drop=input("\t◙ Drop Location : ")

def swargate():
    if drop.upper() == 'KOTHRUD':
        fare = 6.7 * 14
        print('\n\t①','The Distance  From',pick_up.upper(),'➡ ',drop.upper(),'Is 6.7 KM')
        print('\t②',"Fare = ", fare,'₹')
        pass
    elif drop.upper() == 'HADAPSAR':
        fare = 8.8 * 14
        print('\n\t①','The Distance From',pick_up.upper(),'➡ ',drop.upper(),'Is 8.8 KM ')
        print('\t②',"Fare = ", fare,'₹')
    else:
        print("\n\t➤ Sorry, Choose Different Droping Location")


def kothrud():
    if drop.upper()=='SWARGATE':
        fare=6.7*14
        print('\n\t①','The Distance From',pick_up.upper(),'➡ ',drop.upper(),'Is 6.7 KM')
        print('\t②',"Fare = ",fare,'₹')
        pass
    elif drop.upper()=='HADAPSAR':
        fare=15.5*14
        print('\n\t①','The Distance From',pick_up.upper(),'➡ ',drop.upper(),'Is 15.5 KM')
        print('\t②',"Fare = ",fare,'₹')
    else:
        print("\n\t➤ Sorry, Choose Different Droping Location")

def hadapsar():
    if drop.upper() == 'SWARGATE':
        fare = 8.8 * 14
        print('\n\t①','The Distance From',pick_up.upper(),'➡ ',drop.upper(),'Is 8.8 KM')
        print('\t②',"Fare = ", fare,'₹')
        pass
    elif drop.upper() == 'KOTHRUD':
        fare = 15.5 * 14
        print('\n\t①','The Distance From',pick_up.upper(),'➡ ',drop.upper(),'Is 15.5 KM')
        print('\t②',"Fare = ", fare,'₹')
    else:
        print("\n\t➤ Sorry, Choose Different Droping Location")

if pick_up.upper()=='SWARGATE':
    swargate()
    pass
elif pick_up.upper()=='KOTHRUD':
    kothrud()
    pass
elif pick_up.upper()=='HADAPSAR':
    hadapsar()
else:
    print("\n\t➤  Sorry,Our Service Is Not Available On This Location's")