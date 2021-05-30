# on - Question

# Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai 
# unhe count kare. Aur firr unka count print kare.
 
num=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
b=[]
i=0
count=0
while i<len(num):
    a=num[i]
    if a>20 and a<40:
        b.append(a)
        count=count+1  
    i=i+1
print(b,"count",count)