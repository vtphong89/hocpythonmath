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

def kt_cp(n):
    i = 0
    while i ** 2 < n:
        i += 1
    if n == i **2:
        return True
    else:
        return False

def phan_tu_do(b,c):
    if b == 0:
        return ""
    if b == 1  and c == 1:
        return  "+a"
    if b == -1  and c == 1:
        return  "-a"
    if b == 1  and c > 1:
        return  "+ a^{" + str(c) + "}"
    if b == -1  and c > 1:
        return  "- a^{" + str(c) + "}"
    if b > 1  and c == 1:
        return  "+" + str(b) + "a"
    if b > 1  and c > 0:
        return  "+" + str(b) + "a^{" + str(c) + "}"
    if b < -1  and c == 1:
        return  str(b) + "a"
    if b < -1  and c > 0:
        return  str(b) + "a^{" + str(c) + "}"
    else:
        return  str(b) + "a^{" + str(c) + "}"
    
def ham_can_rut_gon(a,b,c,d):
    if a == 1:
        return str(a) + "\\sqrt{" + str(d) + "a^{" + str(c*2) + "}}" + phan_tu_do(b,c)
    if a == - 1:
        return str(a) + "\\sqrt{" + str(d) + "a^{" + str(c*2) + "}}" + phan_tu_do(b,c)
    if d ==  1:
        return str(a) + "\\sqrt{" + "a^{" + str(c*2) + "}}" + phan_tu_do(b,c)
    else:
        return str(a) + "\\sqrt{" + str(d) + "a^{" + str(c*2) + "}}" + phan_tu_do(b,c)
    
    
cau_hoi_mot = beginex() + "Rút gọn các biểu thức sau:\n"
cau_hoi_mot = cau_hoi_mot + itemize_b()
for i in range(1,so_cau+1):
    a = random.choice(range(1,30))
    b = random.choice(range(-20,20))
    c = random.choice(range(1,20))
    d = random.choice(range(1,100)) 
    while kt_cp(d) == False:
        d = random.choice(range(1,100))
    cau_hoi_mot = cau_hoi_mot + "\\item" + " $" + ham_can_rut_gon(a,b,c,d) + "$ với $a>0$ \n"
cau_hoi_mot = cau_hoi_mot + itemize_e() + endex()
print(cau_hoi_mot)

cau_hoi_mot = beginex() + "Rút gọn các biểu thức sau:\n"
cau_hoi_mot = cau_hoi_mot + itemize_b()
for i in range(1,so_cau+1):
    a = random.choice(range(1,30))
    b = random.choice(range(-20,20))
    c = random.choice(range(1,20))
    d = random.choice(range(1,100)) 
    while kt_cp(d) == False:
        d = random.choice(range(1,100))
    cau_hoi_mot = cau_hoi_mot + "\\item" + " $" + ham_can_rut_gon(a,b,c,d) + "$ với $a\leq  0$ \n"
cau_hoi_mot = cau_hoi_mot + itemize_e() + endex()
print(cau_hoi_mot)