detail={"Name":"Sid","Age":21}

for i in detail:
    print(i)
for i in detail:
    print(detail[i])

for i in detail.values():
    print(i)

for i in detail.keys():
    print(i)

detail["Name"]="Siddharth"


backups=detail.copy()
detail.clear()
# print(help(dict))


#Copy one dict to another dict
a={1:20,2:30}
b={3:40,4:45}
for i in b:
    a[i]=b[i]
print(a)


#Count frequency
c=[20,45,6,6,6,7,8,9,1,1,2,3,4,4,4,4,5]
d={}
for i in c:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1

print(d)


#Sum all values

sums=0
for i in d:
    sums+=d[i]
print(f"Sums: {sums}")