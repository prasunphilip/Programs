a=[]
b=[]
c=[]
k=0
n=int(input("Enter total Number of Elements : "))
for i in range(0,n):
	m=int(input("Enter Number : "))
	if (m%2==0):
		a.append(m)
		c.append(m)
	else:
		b.append(m)
		k=k+1
for i in range(0,k):
        c.append(b[i])
print("Even Element list")
print(a)
print("Odd Element list")
print(b)
print("Merge List")
print(c)
c.sort()
print("Sorted List")
print(c)
n=int(input("Enter any value : "))
c.pop(0)
c.insert(0,n)
print("New List")
print(c)
c.sort()
print("Remove Middle Element")
c.pop(2)
print(c)
c.sort()
print("Max Value is ",c[0])
print("Min Value is ",c.pop())
