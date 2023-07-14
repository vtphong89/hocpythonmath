import random

so_cau = 100

# Định nghĩa hàm cần thiết
    ## hàm chuyển log_10 cơ số 10 thành log
def log_co_so(a):
    if a == 10:
        return "\\log"
    if a< 10:
        return "\\log_" + str(a)
    else:
        return "\\log_{" + str(a) + "}"
    ## hàm rút ngắn biểu thức trong log_a(bx+c)
def he_so_b(b):
    if b == 1:
        return "x"
    if b == -1:
        return "-x"
    else:
        return str(b) + "x"
    ## biểu thức bx + c (b khác 0 lúc ta lập while)
def bieu_thuc_loga(b,c):
    if b < 0 and c ==0:
        return "(" + he_so_b(b) + ")"
    if c == 0:
        return he_so_b(b)
    if c>0:
        return "(" + he_so_b(b) + "+" + str(c)  + ")"
    else:
        return "(" + he_so_b(b) + str(c)  + ")"
    ## bieu thức loga không có ngoặc để làm đáp án nhiễu
def bieu_thuc_loga_khong_ngoac(b,c):
    if c == 0:
        return he_so_b(b)
    if c>0:
        return  he_so_b(b) + "+" + str(c)  
    else:
        return he_so_b(b) + str(c) 
    ## hàm số logarit hoàn chỉnh ####LẤY######
def ham_so_loga(a,b,c):
    return "y=" + log_co_so(a) + bieu_thuc_loga(b,c)
    ## tìm ước chung b, c để rút gọn
def uoc_chung(b,c):
    if c ==0:
        return b
    else:
        return uoc_chung(c, b % c)
    ## TẠO RA đáp án CHÍNh
def dao_ham_ham_so_loga(a,b,c):
    he_so_b_dao_ham = int(b/uoc_chung(b,c))
    he_so_c_dao_ham = int(c/uoc_chung(b,c))
    if he_so_b_dao_ham < 0:
        he_so_b_dao_ham = - he_so_b_dao_ham
        he_so_c_dao_ham = - he_so_c_dao_ham
    return "y'=" + "\\dfrac{" + str(he_so_b_dao_ham) + "}" + "{" + bieu_thuc_loga(he_so_b_dao_ham,he_so_c_dao_ham) + "\\ln " + str(a) + "}"
    ## TẠO RA đáp án NHIỄU
def dao_ham_ham_so_loga_sai_mot(a,b,c):
    he_so_b_dao_ham = int(b/uoc_chung(b,c))
    he_so_c_dao_ham = int(c/uoc_chung(b,c))
    if he_so_b_dao_ham < 0:
        he_so_b_dao_ham = - he_so_b_dao_ham
        he_so_c_dao_ham = - he_so_c_dao_ham
    return "y'=" + "\\dfrac{" + str(he_so_b_dao_ham)  + "}" + "{" + bieu_thuc_loga_khong_ngoac(he_so_b_dao_ham,he_so_c_dao_ham) + "}"
def dao_ham_ham_so_loga_sai_hai(a,b,c):
    he_so_b_dao_ham = int(b/uoc_chung(b,c))
    he_so_c_dao_ham = int(c/uoc_chung(b,c))
    if he_so_b_dao_ham < 0:
        he_so_b_dao_ham = - he_so_b_dao_ham
        he_so_c_dao_ham = - he_so_c_dao_ham
    if he_so_b_dao_ham == 1:
        return "y'=" + "\\dfrac{" + "\\ln{" + str(a) + "}}" + "{" + bieu_thuc_loga_khong_ngoac(he_so_b_dao_ham,he_so_c_dao_ham) + "}"
    if he_so_b_dao_ham == -1:
        return "y'=" + "\\dfrac{" + "\\ln{" + str(a) + "}}" + "{" + bieu_thuc_loga_khong_ngoac(he_so_b_dao_ham,he_so_c_dao_ham) + "}"
    else:
        return "y'=" + "\\dfrac{" + str(he_so_b_dao_ham) + "\\ln{" + str(a) + "}}" + "{" + bieu_thuc_loga_khong_ngoac(he_so_b_dao_ham,he_so_c_dao_ham) + "}"
def dao_ham_ham_so_loga_sai_ba(a,b,c):
    he_so_b_dao_ham = int(b/uoc_chung(b,c))
    he_so_c_dao_ham = int(c/uoc_chung(b,c))
    if he_so_b_dao_ham < 0:
        he_so_b_dao_ham = - he_so_b_dao_ham
        he_so_c_dao_ham = - he_so_c_dao_ham
    return "y'=" + "\\dfrac{" + str(he_so_b_dao_ham) + "}" + "{" + "\\ln{" +str(a) + "}}"
print(ham_so_loga(15,5,2))
print(dao_ham_ham_so_loga(15,-5,-10))
 # Bắt đầu viết câu hỏi và đáp án trắc nghiệm
 
ex_cau_hoi = ""
for i in range(1,so_cau+1):
    ## Chọn hệ số
    a = random.choice(range(2,50))
    b = random.choice(range(-5,6))
    c = random.choice(range(-5,6))
    while b == 0:
        b = random.choice(range(-5,6))
    ## Các phương án
    PA1 = "$" + dao_ham_ham_so_loga(a,b,c) +"$"
    PA2 = "$" + dao_ham_ham_so_loga_sai_mot(a,b,c) +"$"
    PA3 = "$" + dao_ham_ham_so_loga_sai_hai(a,b,c) +"$"
    PA4 = "$" + dao_ham_ham_so_loga_sai_ba(a,b,c) +"$"
    lua_chon_phuong_an = [PA1, PA2, PA3, PA4]
## Đề bài và lời giải
    ex_cau_hoi = ex_cau_hoi + "\\begin{ex}\n" + \
    "Đạo hàm của hàm số $" + ham_so_loga(a,b,c) + "$ là\n"\
    "\\choice\n"
    ## Cách trộn phương án
    for i in range(4):
        PA = random.choice(lua_chon_phuong_an)
        if PA == PA1:
            ex_cau_hoi = ex_cau_hoi + "{\\True " + PA + "}\n"
        else:
            ex_cau_hoi = ex_cau_hoi + "{" + PA + "}\n"
        lua_chon_phuong_an.remove(PA)
    ## Ghép lời giải
    ex_cau_hoi = ex_cau_hoi + "\\loigiai{" + \
        "Đạo hàm của hàm số trên là $" + dao_ham_ham_so_loga (a,b,c) +"$." \
            "}\n" +\
            "\\end{ex}\n"
    ## Ghi ra file
fileout = open ("daohamloga.tex", mode ="w" , encoding= "utf-8")
dau = open("khaibao//filedau.tex", encoding= "utf-8").read()
duoi = open("khaibao//filecuoi.tex", encoding= "utf-8").read()  
fileout.write(dau+"\n")
fileout.write(ex_cau_hoi+"\n")
fileout.write(duoi)
fileout.close()