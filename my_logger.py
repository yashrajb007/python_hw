from datetime import date,datetime
import os
class Logger:
    def write(self,msg):
        todays_date=date.today()
        todays_date=todays_date.strftime('%d-%b-%Y')
        msg='\n['+todays_date + " ] "+ msg +" [ "+str(datetime.now())+"]"
        file_name="HW_"+todays_date+".log"
        task=open(file_name,mode='a')
        task.write(msg)
        task.close()