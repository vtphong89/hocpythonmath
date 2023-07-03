import os
import random

# Create the 'data' directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')
    
debai = "\\documentclass[12pt,a4paper]{article}\n" + \
"\\usepackage[utf8]{vietnam}\n" + \
"\\usepackage[top=2.5cm,bottom=2.5cm,left=2cm,right=1.5cm]{geometry}\n" + \
"\\usepackage[loigiai]{ex_test}\n" + \
"\\begin{document}\n" + \
"\\begin{center}\n" + \
"{\\bf\\Large BÀI TẬP TẠO TỰ ĐỘNG}\n" + \
"\\end{center}\n"
socautaora = 1000
for i in range(1,socautaora+1):
    m = random.choice([9,10,11,12,13,14,15])
    n = random.choice([2,3,4,5,6])
    p=m-n
    debai = debai + "\\begin{ex}\n" + \
    "Mẹ chia kẹo cho hai anh em. Em được "+str(m)+" cái kẹo, anh được ít hơn em "+str(n)+" cái kẹo. " + \
    "Hỏi anh được mấy cái kẹo?\n" + \
    "\\\ \\loigiaiEX{\\ \n" + \
    "Số kẹo của anh là $"+str(m)+"-"+str(n)+"="+str(p)+"$.}\n" + \
    "\\end{ex}\n\n"
debai = debai + "\\end{document}"
fileout = open("data/filetaora.tex", mode = "w", encoding = "utf-8")
fileout.write(debai)
fileout.close()