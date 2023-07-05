# Tim phan nguyen, phan vo ti
def my_sqrt(num):
    for i in range(2, num):
        div, mod = divmod(num, i * i)
        if mod == 0:
            sq1, sq2 = my_sqrt(div)
            return [i * sq1, sq2]
        if div == 0:
            break
    return [1, num]
# Rut gon can
def reduce_sqrt(num):
    while num !=1:
        if my_sqrt(num)[0]==1:
            return "$\sqrt{" + str(my_sqrt(num)[1]) + "}$"
        if my_sqrt(num)[1] == 1:
            return "$" + str(my_sqrt(num)[0]) + "$"
        else:
            return "$" + str(my_sqrt(num)[0]) + "\sqrt{" + str(my_sqrt(num)[1]) + "}$"
    return "$1$"

# In ra file tex
import random
debai = "\\documentclass[12pt,a4paper]{article}\n" + \
"\\usepackage[utf8]{vietnam}\n" + \
"\\usepackage[top=2.5cm,bottom=2.5cm,left=2cm,right=1.5cm]{geometry}\n" + \
"\\usepackage{ex_test}\n" + \
"\\begin{document}\n" + \
"\\begin{center}\n" + \
"{\\bf\\Large BÀI TẬP TẠO TỰ ĐỘNG}\n" + \
"\\end{center}\n"
socautaora = 1000
for i in range(1,socautaora+1):
    num = random.choice(range(1,1000))
    debai = debai + "\\begin{ex}\n" + \
    "Rút gọn căn bậc hai của "+str(num)+" ta đươc "+reduce_sqrt(num)+"\n" + \
    "\\end{ex}\n"
debai = debai + "\\end{document}"
fileout = open("reduce_sqrt.tex", mode = "w", encoding = "utf-8")
fileout.write(debai)
fileout.close()