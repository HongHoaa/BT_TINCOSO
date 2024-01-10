import math

def calculate_area(a, b, c):
    # Tính nửa chu vi
    p = (a + b + c) / 2

    # Tính diện tích theo công thức Heron
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return area

# Nhập số đo 3 cạnh từ bàn phím
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Tính diện tích
area = calculate_area(a, b, c)

print("Diện tích tam giác là:", area)
