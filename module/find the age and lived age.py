# find age and days
def age_days(bday_year,current_year):
    age = current_year - bday_year
    days = age * 365

    print("Age:", age)
    print("Days Lived:", days)
bday_year = int(input("Enter Birth Year: "))
current_year = int(input("Enter Current Year: "))
age_days(bday_year, current_year)

# leap years

def age_days(bday_year, current_year):
    age = current_year - bday_year

    leap_count = 0
    for year in range(bday_year, current_year):
        if (year % 4 == 0 and year % 100 != 0):
            leap_count += 1

    days = age * 365 + leap_count

    print("Age:", age)
    print("Days Lived:", days)

bday_year = int(input("Enter Birth Year: "))
current_year = int(input("Enter Current Year: "))

age_days(bday_year, current_year)