import random

so_cau = 100

def begin_ex():
    """Đây là hàm thêm vào begin ex trong latex

    Returns:
        thêm vào 1 chuỗi begin{ex}
    """
    return "\\begin{ex}\n"

def end_ex():
    """Đây là hàm thêm vào END ex trong latex

    Returns:
        thêm vào 1 chuỗi END{ex}
    """
    return "\\end{ex}\n"


cau_hoi = ""
for i in range(1, so_cau +1):
    a  = random.choice(range(1,100))
    b  = random.choice(range(1,100))
    c  = random.choice(range(1,100))
    while a <= b or a <= c or c+b >=a:
        a  = random.choice(range(1,100))
        b  = random.choice(range(1,100))
        c  = random.choice(range(1,100))
    ten_nam = ["Trường", "Huy", "Tuấn", "Đức", "Hoàng", "Minh", "Dũng", "Quang", "Anh", "Cường"]
    ten_nu = ["Thanh", "Lan", "Hương", "Phương", "Linh", "Thúy", "Hạnh", "Ngọc", "Mai", "Thu"]
    ten_nam_nu = ten_nam + ten_nu
    chon_ten = random.sample(ten_nam_nu,3)
    ten_nam_1 = chon_ten[0]
    ten_nam_2 = chon_ten[1]
    ten_nam_3 = chon_ten[2]
    cau_hoi = cau_hoi + begin_ex() + ten_nam_1 + " có " + str(a) + " viên bi. " + ten_nam_1 +  " cho " + ten_nam_2  +" " +str(b) + " viên và cho " + ten_nam_3  + \
         " " +str(c) + " viên bi. Vậy " + ten_nam_1 +" còn lại số viên bi là\n \\choice \n"
    PA1 = "$" + str(a-b-c) + "$ " + "viên bi"
    PA2 = "$" + str (b+c) + "$ " + "viên bi"
    PA3 = "$" + str(a-b) + "$ " + "viên bi"
    PA4 = "$" + str (a-b+c) + "$ " + "viên bi"
    choice_bon = [PA1,PA2,PA3,PA4]
    for i in range(4):
        PA = random.choice(choice_bon)
        if PA == PA1:
            cau_hoi = cau_hoi + "{\\True " + PA + "}\n"
        else:
            cau_hoi = cau_hoi + "{" + PA + "}\n"
        choice_bon.remove(PA)
    ## Ghép lời giải
    cau_hoi = cau_hoi + "\\loigiai{" + \
        "Số viên bi của Nam còn lại là $" + str(a) +"-"+ str(b)+"-"+str(c)+"="+str(a-b-c) +"$." \
            "}\n" + end_ex()
    
    ## Ghi ra file
fileout = open ("vienbi.tex", mode ="w" , encoding= "utf-8")
dau = open("khaibao//filedau.tex", encoding= "utf-8").read()
duoi = open("khaibao//filecuoi.tex", encoding= "utf-8").read()  
fileout.write(dau+"\n")
fileout.write(cau_hoi+"\n")
fileout.write(duoi)
fileout.close()