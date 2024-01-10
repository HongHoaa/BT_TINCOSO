
def so_tu_nhien(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = int(input("Nhập số x: "))
if so_tu_nhien(x):
    print(x, "là số nguyên tố")
else:
    print(x, "không phải là số nguyên tố")