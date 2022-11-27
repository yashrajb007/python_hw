from tabulate import tabulate
fname=input("Enter Your First Name :-")
lname=input("Enter Your Last Name :-")
dob=input("Enter Your Date Of Birth :-")
mobno=int(input("Enter Your Mobile No :-"))
mail=input("Enter Your E-Mail ID :-")

table = [[fname,lname,dob,mobno,mail]]
print(tabulate(table,headers=["First Name","Last Name","Date Of Birth","Mobile No","E-Mail ID"],tablefmt="outline"))
