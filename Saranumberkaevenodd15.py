# Courses
# Login/Signup
# sab-saath-mei
# Sab Saath Mei

# Ek code likho jo kisi bhi list ke liye yeh output karta hai, ki uss list mei odd numbers, even 
# numbers aur sab numbers ka: - count

#     sum
#     average

# print aaye.
# Sample Input


 
list1= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
even=[]
odd=[]
for number in list1:
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
print("list=",list1)
print("odd list",odd)
print("even list",even)
print("sum of odds",sum(odd))
print("sum of evens",sum(even))