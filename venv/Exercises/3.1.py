#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hrs = input('Enter hours ')
rate = input('Enter rate ')
if int(hrs) > 40:
    exthrs = float(hrs) - 40
    extrate = float(rate)*1.5
    pay =  float(hrs) * float(rate) + float(exthrs)*float(extrate)
    print(pay)
else:
    pay = float(hrs) * float(rate)
    print(pay)