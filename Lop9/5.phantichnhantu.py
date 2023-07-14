import random

so_cau = 20

def beginex():
    return "\\begin{ex}\n"

def endex():
    return "\\end{ex}\n"

def itemize_b():
    return "\\begin{enumerate}\n"

def itemize_e():
    return "\\end{enumerate}\n"

def he_so_a(a):
    if a ==1:
        return "x^2 - "
    else:
        return str(a) + "x^2 - "
def he_so_a_nguoc(a):
    if a ==1:
        return " - x^2"
    else:
        return  " - " + str(a) + "x^2"

def ham_nhan_tu_hdt_so_ba(a,b):
    return "{" + he_so_a(a)  + str(b) +"}"

def ham_nhan_tu_hdt_so_ba_nguoc(a,b):
    return   "{" + str(b) + he_so_a_nguoc(a) +"}"

def ham_nhan_tu_hdt_so_mot(b):
    return "{x^2 + 2" + "\\sqrt{" + str(b) + "}x+" + str(b) +"}"

def ham_nhan_tu_hdt_so_hai(b):
    return "{x^2 - 2" + "\\sqrt{" + str(b) + "}x+" + str(b) +"}"

def kt_cp(n):
    i = 0
    while i ** 2 < n:
        i += 1
    if n == i **2:
        return True
    else:
        return False



cau_hoi_mot = beginex() + "Phân tích thành nhân tử:\n"
cau_hoi_mot = cau_hoi_mot + itemize_b()
for i in range(1,so_cau+1):
    a = random.choice(range(1,100))
    b = random.choice(range(1,100))
    while kt_cp(a) == False or kt_cp(b) ==True:
        a = random.choice(range(1,100))
        b = random.choice(range(1,20))
    cau_hoi_mot = cau_hoi_mot + "\\item" + " $" + ham_nhan_tu_hdt_so_ba(a,b) + "$\n"
cau_hoi_mot = cau_hoi_mot + itemize_e() + endex()
print(cau_hoi_mot)

cau_hoi_mot = beginex() + "Phân tích thành nhân tử:\n"
cau_hoi_mot = cau_hoi_mot + itemize_b()
for i in range(1,so_cau+1):
    a = random.choice(range(1,100))
    b = random.choice(range(1,100))
    while kt_cp(a) == False or kt_cp(b) ==True:
        a = random.choice(range(1,100))
        b = random.choice(range(1,20))
    cau_hoi_mot = cau_hoi_mot + "\\item " + "$" + ham_nhan_tu_hdt_so_ba_nguoc(a,b) + "$\n"
cau_hoi_mot = cau_hoi_mot + itemize_e() + endex()
print(cau_hoi_mot)


cau_hoi_mot = beginex() + "Phân tích thành nhân tử:\n"
cau_hoi_mot = cau_hoi_mot + itemize_b()
for i in range(1,so_cau+1):
    b = random.choice(range(1,30))
    while kt_cp(b) == True:
        b = random.choice(range(1,30))
    cau_hoi_mot = cau_hoi_mot + "\\item " + "$" + ham_nhan_tu_hdt_so_mot(b) + "$\n"
cau_hoi_mot = cau_hoi_mot + itemize_e() + endex()
print(cau_hoi_mot)

cau_hoi_mot = beginex() + "Phân tích thành nhân tử:\n"
cau_hoi_mot = cau_hoi_mot + itemize_b()
for i in range(1,so_cau+1):
    b = random.choice(range(1,30))
    while kt_cp(b) == True:
        b = random.choice(range(1,30))
    cau_hoi_mot = cau_hoi_mot + "\\item " + "$" + ham_nhan_tu_hdt_so_hai(b) + "$\n"
cau_hoi_mot = cau_hoi_mot + itemize_e() + endex()
print(cau_hoi_mot)