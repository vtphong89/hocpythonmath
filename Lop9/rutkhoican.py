import random

so_cau = 50

def binh_phuong(a,b):
    return "$\\sqrt{(" + str(a) +"-"+ "\\sqrt{" +str(b)+ "})^2}$\\\\\n"

def binh_phuong_nguoc(a,b):
    return "$\\sqrt{(" + "\\sqrt{" + str(a) + "}" + "-" + str(b) + ")^2}$\\\\\n"

ex_cau_hoi = "Bài 1. Tìm:\\\\\n"
for i in range(1,so_cau+1):
    ## Chọn hệ số
    a = random.choice(range(1,31))
    b = random.choice(range(1,31))
    c = random.choice(range(-15,16))
    while a==0 or b == 0:
        a = random.choice(range(1,31))
        b = random.choice(range(-5,6))
    ex_cau_hoi = ex_cau_hoi + str(i) + ")" + binh_phuong(a,b)

print(ex_cau_hoi)


ex_cau_hoi_hai = "Bài 2. Tìm:\\\\\n"
for i in range(1,so_cau+1):
    ## Chọn hệ số
    a = random.choice(range(1,31))
    b = random.choice(range(1,31))
    c = random.choice(range(-15,16))
    while a==0 or b == 0:
        a = random.choice(range(1,31))
        b = random.choice(range(-5,6))
    ex_cau_hoi_hai = ex_cau_hoi_hai + str(i) + ")" + binh_phuong_nguoc(a,b)

print(ex_cau_hoi_hai)