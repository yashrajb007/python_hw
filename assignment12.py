"""Program For get month from user and print which season belong to that month using conditional statement """
from Color_Console import color
color(text="Blue",bg="white")
print("    Season Of India By Month    ".center(100,'⦾'),"\n")
month = input("\t◙ Enter The Month To Watch Season (e.g. Jan, Feb etc.): ")
month=month.upper()


months = {'JAN':'JANUARY','FEB':'FEBRUARY','MAR':'MARCH','APR':'APRIL','MAY':'MAY','JUN':'JUNE',
        'JUL':'JULY','AUG':'AUGUST','SEP':'SEPTEMBER','OCT':'OCTOBER','NOV':'NOVEMBER','DEC':'DECEMBER'}


if month in ('OCT','NOV','DEC','JAN'):
    season = 'WINTER'
    print(f'\n\t① A {months[month]} Is A {season} Time In India')
    pass
elif month in ('FEB','MAR','APR','MAY'):
    season = 'SUMMER'
    print(f'\n\t① A {months[month]} Is A {season} Time In India')
    pass
elif month in ('JUN','JUL','AUG', 'SEP'):
    season = 'MANSOON'
    print(f'\n\t① A {months[month]} Is A {season} Time In India')
    pass
else:
    print(f'\n\t➤ The {month} Is Not Valid Month')
    
