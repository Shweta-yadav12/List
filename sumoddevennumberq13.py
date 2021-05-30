# Courses
# Login/Signup
# aao-jodein
# Aao Jodein

# Ek code likho jo kissi bhi list ke liye uss list ke do sum ka output karta hai, ki uss 
# list mei odd numbers ka sum aur even numbers ka sum kitna hai.
 
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
a=[]
sum1=0
i=0
sum=0
s=[]
while i<len(elements):
    num=elements[i]
    if num%2==0:
        a.append(num)
        sum1=sum1+num

    else:
        s.append(num)
        sum=sum+num
    i=i+1
print("even",a,"sum",sum1)
print("odd",s,"sum",sum)