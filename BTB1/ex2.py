# BÀI TẬP 2
# Đếm ước số nguyên dương của n
n = 12
def dem_uoc_so(n):
    so_uoc = 0
    for i in range(1, n + 1):
        if n % i == 0:
            so_uoc += 1
    return so_uoc

print(dem_uoc_so(n))

# Liệt kê các ước số vào danh sách
def liet_ke_uoc_so(n):
    uoc_so = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc_so.append(i)
    return uoc_so

print(liet_ke_uoc_so(n))