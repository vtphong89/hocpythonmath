import random

so_cau = 50
## hàm rút ngắn biểu thức trong log_a(bx+c)
def he_so_b(b):
    if b == 1:
        return "x"
    if b == -1:
        return "-x"
    else:
        return str(b) + "x"
    ## biểu thức bx + c (b khác 0 lúc ta lập while)
def bieu_thuc(b,c):
    if b < 0 and c ==0:
        return "(" + he_so_b(b) + ")"
    if c == 0:
        return he_so_b(b)
    if c>0:
        return "(" + he_so_b(b) + "+" + str(c)  + ")"
    else:
        return "(" + he_so_b(b) + str(c)  + ")"
    ## bieu thức loga không có ngoặc để làm đáp án nhiễu
def bieu_thuc_khong_ngoac(b,c):
    if c == 0:
        return he_so_b(b)
    if c>0:
        return  he_so_b(b) + "+" + str(c)  
    else:
        return he_so_b(b) + str(c) 
    


ex_cau_hoi = "Bài 1. Tìm điều kiện của x để căn bậc hai có nghĩa:\\\\\n"
for i in range(1,so_cau+1):
    ## Chọn hệ số
    a = random.choice(range(2,50))
    b = random.choice(range(-15,16))
    c = random.choice(range(-15,16))
    while b == 0:
        b = random.choice(range(-5,6))
    ex_cau_hoi = ex_cau_hoi + str(i) + ")" + "$\\sqrt{" + bieu_thuc_khong_ngoac(b,c) + "}$\\\\\n"

print(ex_cau_hoi)


ex_cau_hoi_hai = "Bài 2. Tìm điều kiện của x để căn bậc hai có nghĩa:\\\\\n"
for i in range(1,so_cau+1):
    ## Chọn hệ số
    a = random.choice(range(2,50))
    b = random.choice(range(-15,16))
    c = random.choice(range(-15,16))
    while b == 0:
        b = random.choice(range(-5,6))
    ex_cau_hoi_hai = ex_cau_hoi_hai + str(i) + ")" + "$\\sqrt{\\dfrac{" + str(a) + "}{" + bieu_thuc_khong_ngoac(b,c) + "}}$\\\\\n"

print(ex_cau_hoi_hai)


ex_cau_hoi_ba = "Bài 3. Tìm điều kiện của x để căn bậc hai có nghĩa:\\\\\n"
for i in range(1,so_cau+1):
    ## Chọn hệ số
    a = random.choice(range(-50,-1))
    b = random.choice(range(-15,16))
    c = random.choice(range(-15,16))
    while b == 0:
        b = random.choice(range(-5,6))
    ex_cau_hoi_ba = ex_cau_hoi_ba + str(i) + ")" + "$\\sqrt{\\dfrac{" + str(a) + "}{" + bieu_thuc_khong_ngoac(b,c) + "}}$\\\\\n"

print(ex_cau_hoi_ba)