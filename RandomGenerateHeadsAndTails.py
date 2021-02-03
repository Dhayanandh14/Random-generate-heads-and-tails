import random
lst=[]
lst2=[]
for i in range(10):
    lst.append(random.choice(["Head","Tails"]))
print(lst)
for j in range(10):
    lst2.append(random.choice(["Head","Tails"]))
print(lst2)
count =0
for k in range(10):
  if lst[k]==lst2[k]:
    count=count+1
print (count)