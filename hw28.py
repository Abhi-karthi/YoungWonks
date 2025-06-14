from datetime import datetime
# dates in string format
str_d1 = []
try:
    year = int(input("What year were you born in?"))
    year = str(year)
    str_d1.append(f"{year}/")
except ValueError:
    print("Please enter a integer.")


try:
    month = int(input("What month were you born in?"))
    month = str(month)
    str_d1.append(f"{month}/")
except ValueError:
    print("Please enter a integer.")

try:
    day = int(input("What day were you born in?"))
    day = str(day)
    str_d1.append(f"{day}")
except ValueError:
    print("Please enter a integer.")

str_d1 = "".join(str_d1)
str_d2 = str(datetime.today())
str_d2 = str_d2.split(" ")[0]

# convert_string to date object
d1 = datetime.strptime(str_d1,"%Y/%m/%d")
d2 = datetime.strptime(str(datetime.today()).split(" ")[0], "%Y-%m-%d")
#difference between dates in timedelta
delta = d2 - d1
print(f"Difference is {delta.days} days")
