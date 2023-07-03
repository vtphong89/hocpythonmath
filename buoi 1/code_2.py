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

socautaora = 100

for i in range(1, socautaora+1):
    problem_type = random.choice(["addition", "subtraction", "multiplication"])
    
    if problem_type == "addition":
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        result = a + b
        
        debai += "\\begin{ex}\n" + \
            "Tính tổng hai số: ${} + {} = ?$\n".format(a, b) + \
            "\\loigiai{\\ \n" + \
            "Ta có: ${} + {} = {}$.\n".format(a, b, result) + \
            "}\n" + \
            "\\end{ex}\n\n"
    
    elif problem_type == "subtraction":
        a = random.randint(1, 100)
        b = random.randint(1, a)
        result = a - b
        
        debai += "\\begin{ex}\n" + \
            "Tính hiệu hai số: ${} - {} = ?$\n".format(a, b) + \
            "\\loigiai{\\ \n" + \
            "Ta có: ${} - {} = {}$.\n".format(a, b, result) + \
            "}\n" + \
            "\\end{ex}\n\n"
    
    elif problem_type == "multiplication":
        a = random.randint(1, 20)
        b = random.randint(1, 10)
        result = a * b
        
        debai += "\\begin{ex}\n" + \
            "Tính tích hai số: ${} \\times {} = ?$\n".format(a, b) + \
            "\\loigiai{\\ \n" + \
            "Ta có: ${} \\times {} = {}$.\n".format(a, b, result) + \
            "}\n" + \
            "\\end{ex}\n\n"

debai += "\\end{document}"

fileout = open("data/filetaora.tex", mode="w", encoding="utf-8")
fileout.write(debai)
fileout.close()
