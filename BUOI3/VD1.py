import random

socau = 100
cau_hoi  = ""
for i in range(1,socau+1):
    PA1 = "Phuong án đúng"
    PA2 = "Phuong án sai 1"
    PA3 = "Phuong án sai 2"
    PA4 = "Phuong án sai 3"
    lua_chon_phuong_an = [PA1, PA2, PA3, PA4]
    cau_hoi = cau_hoi + "\\begin{ex}\n" + \
    " Nội dungg câu hỏi\n" + \
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
duoi = open("khaibao//fileduoi.tex", encoding= "utf-8").read()  
fileout.write(dau+"\n")
fileout.wrile(cau_hoi+"\n")
fileout.write(duoi)
fileout.close()