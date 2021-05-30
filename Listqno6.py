# Courses
# Login/Signup
# Palindrome or not?

# Palindrome wo strings ya numbers hote hai jo ulta seedhe same hote hai. 
# Jaise, NITIN. Nitin ko aap left se padho ya right se, nitin hi hai. Aise hi MOM bhi ek 
# palindrome hai. Code likho jo check kare ki kya list palindrome hai ya nahi. Aur print karo
#  “Haan! palindrome hai” agar hai. Aur “nahi! Palindrome nahi hai” agar nahi hai. Abhi ke liye 
#  iss list ko use kar ke code likh sakte ho:
 
name=[ 'n', 'i', 't', 'i', 'n', ]
new_list=[]
i=1
while i<=len(name):
    new_list.append(name[-i])
    i+=1
# print(new_list)
if new_list==name:
    print("it is palindrome")
else:
    print("it is not palindrome")




