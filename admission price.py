#Admission price

totalcost = 0
age_txt = input('Enter the age of the guest: ')
lenage = len(age_txt)
cost = 0

while lenage != 0:
    age = float(age_txt)
    if age <= 2:
        cost = 0
        totalcost = totalcost + cost
    elif age >= 3 and age <= 12:
        cost = 14.00
        totalcost = totalcost + cost
    elif age > 12 and age < 65:
        cost = 23.00
        totalcost = totalcost + cost
    else:
        cost = 18.00
        totalcost = totalcost + cost
    age_txt = input('Enter the age of the guest: (blank to quit): ')
    lenage = len(age_txt)

print ('The admission cost for the group is:', totalcost, '$')
