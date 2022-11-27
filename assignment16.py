"""Program For get user information and display using functions """
def GetInfo():#fname,lname,dob,bg,city='Pune'):
    print("    User Information    ".center(100,'⦾'),"\n")

def DisplayInfo(fname,lname,dob,bg,city='Pune'):
    return f'My Name IS {fname} {lname},My Date Of Birth {dob},Blood Group {bg} My City Is {city}'


f_name=input("Enter Your First Name : ")
l_name=input("Enter Your Last Name : ")
DOB=input("Enter Your Date Of Birth(E.g 07/01/1998) :")
BG=input("Enter Your Blood Group : ")
City=input("Enter Your City Name : ")


GetInfo()
result=DisplayInfo(f_name,l_name,DOB,BG,City)
print(result) 