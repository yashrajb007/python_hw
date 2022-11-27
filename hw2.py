_fname=input("Enter A First Name: ")
_lname=input("Enter A Last Name: ")
_age=int(input("Enter A Age: "))

print("My Name Is",_fname,_lname,"My Age IS",_age)

print("My Name Is {0} {1} My Age IS {2}".format(_fname,_lname,_age))

print("My Name Is %s %s My Age IS %s"%(_fname,_lname,_age))

print(f"My Name Is {_fname} {_lname} My Age IS {_age}")

print("My Name Is " +str(_fname),str(_lname)+" My Age IS " +str(_age))