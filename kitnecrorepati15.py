# Courses
# Login/Signup
# kitne-crorepati
# Kitne Crorepati? 

# Aapko ek aisa program likhna hai jo, bataye, ki uppar wali list mei kitne log: Jaise, uppar wali
#  list ke liye aapka output hoga:


 
kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
carorepati=0
lakhpati=0
dilwale=0
while i<len(kitna_paisa_hai):
    n=kitna_paisa_hai[i]
    if n<100000:
        dilwale=dilwale+1
    elif n>=100000 and n<10000000:
        lakhpati=lakhpati+1
    elif n>=10000000:
        carorepati=carorepati+1

    i=i+1
print(dilwale,"dilwale")
print(lakhpati,"lakhpati")
print(carorepati,"carorpati")