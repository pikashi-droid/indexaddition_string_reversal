#add index to characters & reverse the string
a=input('enter your string to be reversed: ')
temp=[]
l=list(a)
b=len(l)
for i in range(b):
    n=ord(l[i])
    r=n+i
    alph=chr(r)
    temp.append(alph)
    
k=temp
rev=k[::-1]
print(tostring(rev))

def tostring(a):
    string=''.join(a)
    return (string)


    
    