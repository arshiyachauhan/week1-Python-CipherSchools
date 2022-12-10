a = 1
while a<10:
    print(a)
    a += 1
# iter method defines whether the given object is in sequence
#int object has no attribute __iter__
name ="jatin"
name.__iter__
for c in name:
    print(c)
    print(type(c))
print(type(name))
for i in range(5):
    print(i)
for i in range(5):
    if i == 3:
        continue
    print(i)
for i in range(5):
    print(i)
    if i == 3:
        continue
for i in range(5):
    print(i)
    if i==3:
        break
for i in range(5):
    print(i)
    i=100
for i in range(5):
    print(i)
    i=100
    print(i)
if True:
    #i don"t knows what to do
    pass
#pass is used to create empty blocks
print('rest of the code')
for i in range(5):
    print(i)
else:
    print('something')
for i in range(5):
    print(i)
    if i== 3 :
        break
else:
    print('something')


