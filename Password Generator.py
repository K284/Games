import random
# min 2 ucase
# min 2 lcase
# min 2 punctuation
# min 2 digits

def shuffle(x):
    l = list(x)
    random.shuffle(l)
    return ''.join(l)

d = [1,2,3,4,5,6,7,8,9,0]
p = ['~','`','!','@','#','$','%','^','&','*','(',')','_','+','/','*','-','+','.','<','>','?',':','=',';',',']

uc1 = chr(random.randint(65,90))
uc2 = chr(random.randint(65,90))
lc1 = chr(random.randint(65,90)).lower()
lc2 = chr(random.randint(65,90)).lower()
d1 = str(random.choice(d))
d2 = str(random.choice(d))
p1 = random.choice(p)
p2 = random.choice(p)

password= uc1+uc2+lc1+lc2+d1+d2+p1+p2
password = shuffle(password)
print(password)
