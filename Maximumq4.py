# Login/Signup
# submission_type: url

# Code likho jo iss list mein se second maximum element (doosra sabse bada element) dhund kar
#  kar print kare.
 
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7] 

# Iss list ke liye apke program ka output 56 hona chaiye.
# Edit on Github


number=[50,40,23,70,56,12,5,10,7]
a=[]
i=0
b=number[0]
while i<len(number):
    c=number[i]
    if  number[i]>b:
        a.append(c)
    i=i+1
print(a)


