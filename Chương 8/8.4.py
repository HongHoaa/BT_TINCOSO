a = eval(input("nhập độ dài cạnh a: "))
b = eval(input("nhập độ dài cạnh b: "))
c = eval(input("nhập độ dài cạnh c: "))

if a+b>c and b+c>a and c+a>b:
    print("đây là một tam giác")
    
    from math import sqrt
    p = (a+b+c)/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    print("diện tích của tam giác trên là: ",S)
else:
    print("đây không phải một tam giác")

