n=int(input("Up to which natural number ?"))
ctr=1
sum_even=sum_odd=0
while ctr<=n:
    if ctr%2==0:
        sum_even+=ctr
    else:
        sum_odd+=ctr
    ctr+=1
print("The sum of even integer is",sum_even)
print("The sum of odd integer is",sum_odd)
# dry run is not done.
