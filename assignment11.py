"""Program For Print dictionary in tabular format  """
'''Dictionary Of Empolyee'''


employee={'empId':[1,2,3],'name':['A','B','C']}
print(" Information Of Emplyee ".center(60,'*'),"\n")
print("Employee ID\t\tEmployee Name\n".center(54))
for a in range(len(employee['empId'])):
    for i,j in employee.items():
        print(f'{j[a]}'.center(30),end='')
    print('')
print('\n',"".center(60,'*'),"\n")





'''Dictionary Of Vehicle Info'''

vehicle_info={'Vehicle No':['MH09FC2552','MH46N3443','MH12AX7007'],'Type':['2-Wheeler','4-Wheeler','4-Wheeler'],
            'Passing':['Kolhapur','Navi Mumbai','Pune']}
print("\n"," Information Of Vehicle ".center(60,'*'),"\n")
print("Vehicle No\t\tType\t\t\tPassing\n")
for a in range(len(vehicle_info['Vehicle No'])):
    for i,j in vehicle_info.items():
        print(f'{j[a]}\t\t',end='')
    print()
print('\n',"".center(60,'*'),"\n")




'''Dictionary Of Bank Account Information'''


bank_info={'Account No':['122501001972','122501001979','122501009899','122578945612'],
            'Account  Holder':['Nikhil Mane','Yashraj Bhosale','Aniket Patil','Sanket Desai'],
            'Account Type':['Saving','Current','Demat','Loan'],
            'Branch':['Kavrnagar','Pimpari','Hadapsar','Shivaji Nagar']
            }
print("\n"," Information Of Bank Account ".center(75,'*'),"\n")
print("Account Number\t\tAccount Holder\t\tAccount Type\tBranch\n")
for a in range(len(bank_info['Account No'])):
    for i,j in bank_info.items():
        print(f'{j[a]}\t\t',end='')
    print()
print('\n',"".center(75,'*'),"\n")


'''Dictionary Of Mobile Info'''


mob_info={'Brand':['Apple','Samsung','OnePlus','Oppo','Vivo'],
            'Mobile Name':['Iphone14+','S22 Ultra','10t     ','Reno 6   ','V25     '],
            'Launch Date':['September 2022','May 2022','June 2022','June 2022','October 2022'],
            'Price':['89900','99999','60000','35000','35000']
            }
print("\n"," Information Of Mobile's ".center(75,'*'),"\n")
print("Brand\t\tMobile Name\t\tLaunch Date\t\tPrice\n")
for a in range(len(mob_info['Brand'])):
    for i,j in mob_info.items():
        print(f'{j[a]}\t\t',end='')
    print()
print('\n',"".center(75,'*'),"\n")




'''Dictionary Of Student Info'''


stud_info={'Student Name':['Ramesh Koli','Suresh Shinde','Ganesh Gaitonde','Prachi Shah','Kranti Patil'],
            'Class':['BSC-I','BCOM-II','ARTS-I','BSC-III','ARTS-II'],
            'Roll No':['7625','5298','3569','8995','4126'],
            'Fee':['15000','3000','500','3000','6000'],
            'Mobile No':['9874561230','8985758985','7755664562','8795231400','9960460914']
            }
print("\n"," Information Of Student's".center(75,'*'),"\n")
print("Student Name\t\tClass\t\tRoll No\t\tFee\t\tMobile No\n")
for a in range(len(stud_info['Student Name'])):
    for i,j in stud_info.items():
        print(f'{j[a]}\t\t',end='')
    print()
print('\n',"".center(75,'*'),"\n")
