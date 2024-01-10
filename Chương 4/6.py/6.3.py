def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

so_a = int(input("Nhập số a: "))
so_b = int(input("Nhập số b: "))

ket_qua = gcd(so_a, so_b)

print("Ước số chung lớn nhất của", so_a, "và", so_b, "là:", ket_qua)


