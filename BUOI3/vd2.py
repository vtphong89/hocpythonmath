import random

socau = 100
cau_hoi  = ""
for i in range(1,socau+1):
    def kiem_tra(a,b,c,d):
        if a != b and a != c and a != d and b != c and b != d and c != d:
            return True
        else:
            return False
    a = random.choice(range(-3,3))
    b = random.choice(range(-3,3))
    while kiem_tra(a,b,-a,-b) == False:
        a = random.choice(range(-3,3))
        b = random.choice(range(-3,3))
    PA1 = "$" + str(a) +"$"
    PA2 = "$" + str(-a) +"$"
    PA3 = "$" + str(b) +"$"
    PA4 = "$" + str(-b) +"$"
    lua_chon_phuong_an = [PA1, PA2, PA3, PA4]
    cau_hoi = cau_hoi + "\\begin{ex}\n" + \
    " Trên mặt phẳng tọa độ, cho $M(" + str(a) + "," + str(b) + ")$ là điểm biểu diển của số phức $z$. Phần thực của số phức $z$ là\n" + \
    "\\choice\n" 
    for i in range(4):
        PA = random.choice(lua_chon_phuong_an)
        if PA == PA1:
            cau_hoi = cau_hoi + "{\\True " + PA + "}\n"
        else:
            cau_hoi = cau_hoi + "{" + PA + "}\n"
        lua_chon_phuong_an.remove(PA)
    cau_hoi = cau_hoi + "\\loigiai{" + \
        "Noi dung loi giai.\n" + \
            "}\n" +\
            "\\end{ex}\n"
fileout = open ("vidumau.tex", mode ="w" , encoding= "utf-8")
dau = open("khaibao//filedau.tex", encoding= "utf-8").read()
duoi = open("khaibao//filecuoi.tex", encoding= "utf-8").read()  
fileout.write(dau+"\n")
fileout.write(cau_hoi+"\n")
fileout.write(duoi)
fileout.close()