import calendar

thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))

so_ngay = calendar.monthrange(nam, thang)[1]

print("Số ngày của tháng {} năm {} là: {}".format(thang, nam, so_ngay))