# A = tổng các số lẻ nhỏ hơn hoặc bằng n
# B = tổng các số chẵn nhỏ hơn hay bằng n
# C = tích các số từ 1 đến n
# D = tích các số chia hết cho 3
# E = tổng các cố nguyên tố nhỏ hơn hay bằng n
# F = tổng chuỗi đan dấu

def main():
    n = int(input("Nhập n: "))

    tong_so_le = 0
    for i in range(1, n + 1):
        if i % 2 == 1:
            tong_so_le += i

    tong_so_chan = 0
    for i in range(2, n + 1, 2):
        tong_so_chan += i

    tich_cac_so = 1
    for i in range(1, n + 1):
        tich_cac_so *= i

    tich_cac_so_chia_het_cho_3 = 1
    for i in range(1, n + 1):
        if i % 3 == 0:
            tich_cac_so_chia_het_cho_3 *= i

    tong_cac_so_nguyen_to = 0
    for i in range(2, n + 1):
        if is_prime(i):
            tong_cac_so_nguyen_to += i

    tong_chuoi_dan_dau = 0
    for i in range(1, n + 1):
        tong_chuoi_dan_dau += i * (-1) ** i

    print("A = ", tong_so_le)
    print("B = ", tong_so_chan)
    print("C = ", tich_cac_so)
    print("D = ", tich_cac_so_chia_het_cho_3)
    print("E = ", tong_cac_so_nguyen_to)
    print("F = ", tong_chuoi_dan_dau)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    main()