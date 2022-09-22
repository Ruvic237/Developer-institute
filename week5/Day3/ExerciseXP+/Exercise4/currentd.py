#program to obtain current date

from datetime import date

def Show_Date(): #function to show currrent date only
    heute = date.today()
    print(f"The date of today is:{heute}")
Show_Date()
