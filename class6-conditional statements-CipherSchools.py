a=True
if a:
    print("the value is true")
print("end")
a=False
if a:
    print("this value is true")
else:
    print("this value is false")
a=5
if a==3:
    print('this value is 3')
elif a==5:
    print('this value is 5')
else:
    print('this value is not 3 or 5')
#x: int (-inf,inf)
#G --> x
#a-x < 0
#b-x == 0
#c-x > 0
#a int b = b int c = a int c = phi
#a u b u c = G 
#conditions are mutually exclusive
#if
#elif
#else
#solving k map question-
# q=can A acess profile of B
# a= isFriend
# b= isBlocked
# c= isAdmin
# d= isMarkzuckerberg
# create truth table
# a b c d q
# 0 0 0 0 0
# 0 0 0 1 1
# 0 0 1 0 1
# 0 0 1 1 1
# 0 1 0 0 0
# 0 1 0 1 1
# 0 1 1 0 0
# 0 1 1 1 1
# 1 0 0 0 1
# 1 0 0 1 1
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 0 0 0
# 1 1 0 1 1
# 1 1 1 0 0
# 1 1 1 1 1
#if .......:
#   print(" has access")
#else:
# print("access denied ")




