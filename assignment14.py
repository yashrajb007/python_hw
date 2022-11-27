"""Program For Temprature Conversion From Celsius To Fahrenheit & Kelvin"""
from Color_Console import color
color(text="Blue",bg="white")
from my_logger import Logger 

try : 
    log=Logger()
    print("    Convert Temperature Celsius(°C) To Fahrenheit(°F)     ".center(100,'⦾'),"\n")
    print(" Choose Conversion ".center(100,'*') )
    print("\n\t\t1] Celsius(°C) To Fahrenheit(°F)")
    print("\t\t2] Fahrenheit(°F) To Celsius(°C) ")
    
    choice=int(input("\n\t\t◙ Enter Your Choice [1,2] = "))
    log.write(f'Entered Choice = {choice}')
    print()
    
    if choice==1:
        temp=int(input("\n◙ Enter Temperature In Celsius (°C) : "))
        print(" Celsius(°C) To Fahrenheit(°F) ".center(100,'⦾'))
        print(f'\n\t\t① {temp}°C Celsius = {temp*1.8+32}°F Fahrenheit')
        log.write(f'Entered Temprature = {temp} And Converted Temprature = {temp*1.8+32}')
    elif choice==2:
        temp=int(input("\n\t\t◙ Enter Temperature In Fahrenheit(°F) : "))
        print("\n\t\tFahrenheit(°F) To Celsius(°C)".center(100,'⦾'))
        print(f'\n\t\t① {temp}°F Fahrenheit = {(temp-32)/1.8000} Celsius(°C)')
        log.write(f'Entered Temprature = {temp} And Converted Temprature{(temp-32)/1.8000}')
    else:
        print("\n\t\t➤ Enter Valid Choice[1,2]")


except BaseException as ex:
    print(ex)