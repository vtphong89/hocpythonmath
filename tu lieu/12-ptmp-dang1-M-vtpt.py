import sympy
import re
import random
import os
import subprocess

#số lượng bài tập
num_exercises = 100

#định nghĩa hàm làm đẹp
def replace_zeros(expression):
    pattern = r'(\+|-)0(\d*[xyz](\^\d+)?)?'
    return re.sub(pattern, ' ', expression)

#list bài tập
exercises = []

#lập trình phép toán - khai báo biến M(a,b,c) và dx+ey+fz+g=0
for i in range(num_exercises):
    a, b, c, d, e, f = random.sample(range(-5, 5), 6)
    
    #PTMP ax+by+cz+g=0
    g = -a*d-b*e-c*f
    
    #rút gọn biểu thức
    x = sympy.simplify(g)
    
    #bien nhiễu
    x_1 = x+1
    x_2 = x+2
    x_3 = x+3
    #4 đáp án 
    z_0 = f'(P)\colon {a}x+{b}y+{c}z+{x}=0'
    z_1 = f'(P)\colon {a}x+{b}y+{c}z+{x_1}=0'
    z_2 = f'(P)\colon {a}x+{b}y+{c}z+{x_2}=0'
    z_3 = f'(P)\colon {a}x+{b}y+{c}z+{x_3}=0'
    
    # Các phương án z, z_1, z_2, z_3
    options = [z_0, z_1, z_2, z_3]

    # Chọn ngẫu nhiên 4 phương án trong list options
    random_options = random.sample(options, 4)

    # Thêm \True vào phương án đúng và trộn nó lại
    question = f'\\begin{{ex}} \nTrong không gian với hệ tọa độ $Oxyz$, viết phương trình mặt phẳng biết nó đi qua điểm $M({d};{e};{f})$ và vecto pháp tuyến $n({a};{b};{c})$.\n \\choice\n'
    for i, option in enumerate(random_options):
        if option == z_0:
            question += f"{{ \\True ${option}$ }}\n"
        else:
            question += f"{{ ${option}$ }}\n"
    question += ' \\end{ex}\n'

    # Làm đẹp câu hỏi
    question = question.replace('\\frac', '\\dfrac').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x').replace('1x', 'x').replace('1y', 'y').replace('1z', 'z').replace('0x', ' ')
    question = replace_zeros(question)
    # xử lý cộng đầu dòng
    question = question.replace('$(P)\colon  +', '$(P)\colon ')
    # Lưu câu hỏi vào list exersises
    exercises.append(question)

# Đường dẫn đến thư mục chứa file "khoangcach1diem.tex"
folder_path = "D:/DAY ONLINE/MAIN ONLINE 12/data/"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
# Tên file để lưu bài tập
file_name = "12-ptmp-dang-1-M-vtpt.tex"

# Đường dẫn đầy đủ đến file bài tập
file_path = os.path.join(folder_path, file_name)

# Ghi các bài tập vào file
with open(file_path, "w", encoding="utf-8") as f:
    for i, exercise in enumerate(exercises):
        f.write(f"%Exercise {i+1}:\n{exercise}\n\n")
    
print(f"Đã lưu bài tập vào file {file_path}\n \\input{{data/{file_name}}}")
# Mở thư mục
subprocess.Popen(f'explorer {os.path.realpath(folder_path)}')

