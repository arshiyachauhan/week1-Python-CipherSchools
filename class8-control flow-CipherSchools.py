n=5
for i in range(n):
    for j in range(n):
        print(i, end= " ")
    print()
# n-i gives distance from bottom
# i+1 gives distance from top
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()

for i in range(n):
    for j in range(n):
        print(n-j,end=" ")
    print()
#n-j gives distance from right
#j+1 gives distance from left most wall
#put n-j-1 to get perfect reverse-(4 3 2 1 0...)
n=7
for i in range(n):
    for j in range(n):
        print(max(i+1,j+1,n-i,n-j), end =" ")
    print()
#to merge two matrices together
#solving it for lower right corner-
n=5
for i in range (n):
    for j in range(n):
        print(max(i,j),end=" ")
    print()
for i in range(n):
    for j in range(n):
        print (
            max(max(i+1,j+1),max(n-j,n-i)), end = " ")
    print()

