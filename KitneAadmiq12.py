# Courses
# Login/Signup
# kitne-aadmi-the
# Kitne Aadmi The

# Ek code likho jo kisi bhi list ke liye yeh output karta hai, ki uss list mei kitne odd numbers
#  hai aur kitne even numbers hai.
 
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
list1=[]
list2=[]
i=0
while i<len(elements):
    m=elements[i]
    if m%2==0:
        list1.append(m)
    else:
        list2.append(m)
    i=i+1
print("no is divisible by 2",list1)
print("no is not divisible by",list2)