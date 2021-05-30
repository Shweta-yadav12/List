# Courses
# Login/Signup
# submission_type: url
# Is Magic Square?

# Magic Square woh square hota hai jismei - har row ka, har column ka, and dono diagonals ka sum same
#  hota hai. Aapko yeh program likhna hai - jo ek nested list leta hai, aur dekhta hai ki woh magic 
#  square hai ya nahi? E.g. Yeh magic square hai, kyuki
 

magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
] 
i=0
sum1=0
while i<len(magic_square):
    r=0
    while r<len(magic_square[i]):
        sum1=sum1+magic_square[i][r]
    r=r+1
i=i+1
print(sum1)
a=0
sum2=0
while a<len(magic_square):
    c=0
    while c<len(magic_square[a]):
        sum2=sum2+magic_square[c][a]
        c=c+1
    a=a+1
print(sum2)
b=0
sum3=0
while b<len(magic_square):
    d=0
    while d<len(magic_square[b]):
        sum3=sum3+magic_square[d][d]
        d=d+1
    b=b+1
print(sum3)
if sum1==sum2==sum3:
    print("magic square")
else:
    print("not magic square")


        
    