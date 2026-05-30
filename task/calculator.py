

import datetime
def calculate_birthday(birth_year,birth_month,birth_Day) :
    today =  datetime.date.today()

    birth_date =  datetime.date(birth_year,birth_month,birth_Day)

    if birth_date > today :
        return f"your not put futute date: try again!"
    
    years =  today.year -  birth_date.year
    days =  today.day -    birth_date.day
    month =  today.month -  birth_date.month

    if days < 0 :
        first_date =  datetime.date(today.year,today.month,1)
        last_date =  first_date -  datetime.timedelta(days = 1)
        days += last_date.day
        month -= 1


    if month < 0 :
        month =+ 12
        years -= 1


    return f"your Years : {years},your Month : {month} and days : {days}"


years =  int(input("enter your years : (e.g : 2005)"))
day = int(input("enter your days : (e.g : 20)"))
month = int(input("enter your month : (e.g : 12) "))

result =  calculate_birthday(years,month,day)
print(result)




