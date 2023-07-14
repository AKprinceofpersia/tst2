import math

print("be barname ye tabdil saniye be zaman khosh amadid")
timesec=int(input("addad ra be sanie vared konid: "))
if timesec>=60:
    if timesec>=3600:
        second2=timesec%60
        minute2=int((timesec%3600)//60)
        hour1=int(timesec/3600)
        print(hour1,"hours",minute2,"minutes and",second2,"second")
    elif timesec<3600:
        second1=timesec%60
        minute1=int(timesec/60)
        print(minute1,"minutes and",second1,"second")
elif timesec<60:
    print(timesec)