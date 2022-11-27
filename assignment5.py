'''Program for String Concatination Of Vehicle No'''
from tabulate import tabulate
print("********** Vehicle Numbering System *********")
vehicle_no=input("Enter Vehicle No : ")
table=[["State",vehicle_no[0:2].upper()],["District Code",vehicle_no[2:4]],["Series",vehicle_no[4:6].upper()],["Actual Number",vehicle_no[6:]]]
print(tabulate(table,tablefmt='grid'))
# print("State = ",vehicle_no[0:2].upper())
# print("District Code = ",vehicle_no[2:4])
# print("Series = ",vehicle_no[4:6].upper())
# print("Actual Number= ",vehicle_no[6:])
