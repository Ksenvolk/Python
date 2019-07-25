#Rewrite your pay program using try and except so that your program handles non-numeric input
# gracefully by printing a message and exiting the program. The following shows two executions of the program:

inp1 = input('Enter hours ')
inp2 = input('Enter rate ')
try:
    hrs = float(inp1)
    rate = float(inp2)
except:
    print('Error, please enter numeric input')
    quit()
if hrs > 40:
    exthrs = hrs - 40
    extrate = rate*1.5
    pay =  hrs * rate + exthrs* extrate
    print(pay)
else:
    pay = hrs * rate
    print(pay)