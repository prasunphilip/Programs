import time
import random
inputt=int(input("Enter Max Input Size : "))
bucket_size=int(input("Enter Bucket Size : "))
outgoing=int(input("Enter Rate of Output Size : "))
n=int(input("Enter number of turns : "))
store=0

print("\n")

while(n!=0):
    input_size = random.randrange(0,inputt,1)
    print("The Incoming Size is ", input_size)
    if(input_size<=(bucket_size-store)):
        store=store+input_size
        print("Bucket Buffer Size is ", store ," out of ", bucket_size)
    else:
        print("Packet Loss : ",(input_size-(bucket_size-store)))
        store=bucket_size
        print("Bucket Buffer Size is ", store ," out of ", bucket_size)
    store=store-outgoing
    print("After outgoing : ",store," left out of ",bucket_size)
    n=n-1
    time.sleep(1)
    print("\n")
