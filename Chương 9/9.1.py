def sign(x):
    if x<0:
        s=-1
    if x>0:
        s=1
    if x==0:
        s=0
    return s
x=int(input("nhập số:"))
print(sign(x))