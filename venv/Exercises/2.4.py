## Assume that we execute the following assignment statements:
#
# width = 17
# height = 12.0
#
# For each of the following expressions, write the value of the expression and
# the type (of the value of the expression).
#
#   1. width / 2
#   2. width / 2.0
#   3. height / 3
#   4. 1 + 2 * 5
#
# Use Python interpreter to check your answers.

width = 17
height = 12.0

a = width//2
b = width/2.0
c = height/3
d = (a + b)*5
print(a,b,c,d)

print(type(a))   #<type 'int'>
print(type(b))  #<type 'float'>
print(type(c))   #<type 'float'>
print(type(d))    #<type 'int'>