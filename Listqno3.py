

# Max Element

# Code likho jo iss list mein se maximum dhund kar ke print kare.
 
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 

# Iss list ke liye aapke program ka output 70 hona chaiye


number= [50,40,23,70,56,12,5,10,7]
i=0
b=[]
a=number[0]
while i<len(number):
    if number[i]>a:
        a=number[i]
    i=i+1
print(a)



   