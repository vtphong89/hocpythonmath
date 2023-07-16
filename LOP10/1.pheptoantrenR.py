import random

so_cau = 50

def begin_ex():
    """Đây là hàm thêm vào begin ex trong latex

    Returns:
        thêm vào 1 chuỗi begin{ex}
    """
    return "\\begin{ex}\n"

def end_ex():
    return "\\end{ex}\n"

def begin_item():
    return "\\begin{enumerate}\n"

def end_item():
    return "\\end{enumerate}\n"


def khoang_ab(a,b):
    if a == -14:
        return "(-\\infty" + ";" + str(b) + ")"
    if b == 14:
        return "(" + str(a) + ";" + "+ \\infty)"
    else:
        return "(" + str(a) + ";" + str(b) + ")"
    
def doan_ab(a,b):
     return "[" + str(a) + ";" + str(b) + "]"
 
def khoang_doan_ab(a,b):
    if a == -14:
        return "(-\\infty" + ";" + str(b) + "]"
    else:
        return "(" + str(a) + ";" + str(b) + "]"
    
def doan_khoang_ab(a,b):
    if b == 14:
        return "[" + str(a) + ";" + "+ \\infty)"
    else:
        return "[" + str(a) + ";" + str(b) + ")"


cau_hoi_mot = begin_ex() + "Vẽ trục và tìm:\n"
cau_hoi_mot = cau_hoi_mot + begin_item()
for i in range(1,so_cau+1):
    a = random.choice(range(-14,15))
    b = random.choice(range(-14,15))
    c = random.choice(range(-14,15))
    d = random.choice(range(-14,15))
    while a>=b or c>=d or c>b or b>d:
        a = random.choice(range(-14,15))
        b = random.choice(range(-14,15))
        c = random.choice(range(-14,15))
        d = random.choice(range(-14,15))
    e = random.choice([khoang_ab(a,b),doan_ab(a,b),khoang_doan_ab(a,b),doan_khoang_ab(a,b)])
    f = random.choice([khoang_ab(c,d),doan_ab(c,d),khoang_doan_ab(c,d),doan_khoang_ab(c,d)])
    cau_hoi_mot = cau_hoi_mot + "\\item" + " $" + e + "\\cup" + f + "$\n"
cau_hoi_mot = cau_hoi_mot + end_item() + end_ex()
print(cau_hoi_mot)

cau_hoi_mot = begin_ex() + "Vẽ trục và tìm:\n"
cau_hoi_mot = cau_hoi_mot + begin_item()
for i in range(1,so_cau+1):
    a = random.choice(range(-14,15))
    b = random.choice(range(-14,15))
    c = random.choice(range(-14,15))
    d = random.choice(range(-14,15))
    i = random.choice(range(-14,15))
    j = random.choice(range(-14,15))
    while a>=b or c>=d or c>b or b>d or i>=j or i>=b or i<=c:
        a = random.choice(range(-14,15))
        b = random.choice(range(-14,15))
        c = random.choice(range(-14,15))
        d = random.choice(range(-14,15))
        i = random.choice(range(-14,15))
        j = random.choice(range(-14,15))
    e = random.choice([khoang_ab(a,b),doan_ab(a,b),khoang_doan_ab(a,b),doan_khoang_ab(a,b)])
    f = random.choice([khoang_ab(c,d),doan_ab(c,d),khoang_doan_ab(c,d),doan_khoang_ab(c,d)])
    g = random.choice([khoang_ab(i,j),doan_ab(i,j),khoang_doan_ab(i,j),doan_khoang_ab(i,j)])
    cau_hoi_mot = cau_hoi_mot + "\\item" + " $" + e + "\\cup" + f + "\\cup" + g + "$\n"
cau_hoi_mot = cau_hoi_mot + end_item() + end_ex()
print(cau_hoi_mot)

cau_hoi_mot = begin_ex() + "Vẽ trục và tìm:\n"
cau_hoi_mot = cau_hoi_mot + begin_item()
for i in range(1,so_cau+1):
    a = random.choice(range(-14,15))
    b = random.choice(range(-14,15))
    c = random.choice(range(-14,15))
    d = random.choice(range(-14,15))
    while a>=b or c>=d or c>b or b>d:
        a = random.choice(range(-14,15))
        b = random.choice(range(-14,15))
        c = random.choice(range(-14,15))
        d = random.choice(range(-14,15))
    e = random.choice([khoang_ab(a,b),doan_ab(a,b),khoang_doan_ab(a,b),doan_khoang_ab(a,b)])
    f = random.choice([khoang_ab(c,d),doan_ab(c,d),khoang_doan_ab(c,d),doan_khoang_ab(c,d)])
    cau_hoi_mot = cau_hoi_mot + "\\item" + " $" + e + "\\cap" + f + "$\n"
cau_hoi_mot = cau_hoi_mot + end_item() + end_ex()
print(cau_hoi_mot)


cau_hoi_mot = begin_ex() + "Vẽ trục và tìm:\n"
cau_hoi_mot = cau_hoi_mot + begin_item()
for i in range(1,so_cau+1):
    a = random.choice(range(-14,15))
    b = random.choice(range(-14,15))
    c = random.choice(range(-14,15))
    d = random.choice(range(-14,15))
    i = random.choice(range(-14,15))
    j = random.choice(range(-14,15))
    while a>=b or c>=d or c>b or b>d or i>=j or i>=b or i<=c:
        a = random.choice(range(-14,15))
        b = random.choice(range(-14,15))
        c = random.choice(range(-14,15))
        d = random.choice(range(-14,15))
        i = random.choice(range(-14,15))
        j = random.choice(range(-14,15))
    e = random.choice([khoang_ab(a,b),doan_ab(a,b),khoang_doan_ab(a,b),doan_khoang_ab(a,b)])
    f = random.choice([khoang_ab(c,d),doan_ab(c,d),khoang_doan_ab(c,d),doan_khoang_ab(c,d)])
    g = random.choice([khoang_ab(i,j),doan_ab(i,j),khoang_doan_ab(i,j),doan_khoang_ab(i,j)])
    cau_hoi_mot = cau_hoi_mot + "\\item" + " $" + e + "\\cap" + f + "\\cap" + g + "$\n"
cau_hoi_mot = cau_hoi_mot + end_item() + end_ex()
print(cau_hoi_mot)