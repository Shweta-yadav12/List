# duplicates
# Duplicates

# iss lists mei se duplicates nikal kar, kisi aur list mei daal kar print karne hai.

a= [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11] 
i=0
b=[]
# count=0
while i<len(a):
    l=a[i]
    if l not in b:
        b.append(l)
        # count=count+1
    i=i+1
print(b)