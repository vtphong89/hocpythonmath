import sympy
import re
import random
import os
import subprocess

#số lượng bài tập
num_exercises = 2

#định nghĩa hàm làm đẹp
def replace_choiceeros(expression):
    pattern = r'(\+|-)0(\d*[xyz](\^\d+)?)?'
    return re.sub(pattern, ' ', expression)

#list bài tập
exercises = []

#Dạng 1. Tổng quát cho số lẻ
print("\nDạng 1:\n")
#lập trình phép toán - khai báo biến (x-a)/e=(y-b)/f=(z-c)/g
for i in range(num_exercises):
    a, b, c = random.sample(range(-5, 5), 3)
    #Kiểm tra  e,f,g khác không
    e = 0
    while e == 0:
        e = random.randint(-5, 5)*2
    f = 0
    while f == 0:
        f = random.randint(-5, 5)*2
    g = 0
    while g == 0:
        g = random.randint(-5, 5)*2
    #Kiểm tra e,f,g để rút gọn còn lại thì trả giá trị cũ
    if (e % 2 == 0 and f % 2 == 0 and g % 2 == 0):
        e = e//2
        f = f//2
        g = g//2
    
    
    #Đáp Án Trắc Nghiệm
        choice_0 = f'({e};{f};{g})'
        choice_1 = f'({-e};{-f};{g})'
        choice_2 = f'({e};{-f};{-g})'
        choice_3 = f'({-e};{f};{-g})'
    
    # Các phương án choice_0, choice_1, choice_2, choice_3
    options = [choice_0, choice_1, choice_2, choice_3]

    # Chọn ngẫu nhiên 4 phương án trong list options
    random_options = random.sample(options, 4)

    # Thêm \True vào phương án đúng và trộn nó lại
    question = f'\\begin{{ex}} \nCho đường thẳng $d\\colon \\dfrac{{x-{a}}}{{{e}}}=\\dfrac{{y-{b}}}{{{f}}}=\\dfrac{{z-{c}}}{{{g}}}$.   Đường thẳng  $d$  có một véctơ chỉ phương là\n \\choice\n'
    for i, option in enumerate(random_options):
        if option == choice_0:
            question += f"{{ \\True ${option}$ }}\n"
        else:
            question += f"{{ ${option}$ }}\n"
    question += ' \\end{ex}\n'

    # Làm đẹp câu hỏi
    question = question.replace('\\frac', '\\dfrac').replace('--', '+').replace('-+', '-').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x').replace('1x', 'x').replace('1y', 'y').replace('1choice', 'choice').replace('0x', ' ')
    question = replace_choiceeros(question)
    # xử lý cộng đầu dòng
    question = question.replace('$(P)\colon  +', '$(P)\colon ')
    # Lưu câu hỏi vào list exersises
    exercises.append(question)

    print(question)


#Dạng 1.1. Tổng quát cho số lẻ - đối
print("\nDạng 1.1:\n")
#lập trình phép toán - khai báo biến (x-a)/e=(y-b)/f=(z-c)/g
for i in range(num_exercises):
    a, b, c = random.sample(range(-5, 5), 3)
    #Kiểm tra  e,f,g khác không
    e = 0
    while e == 0:
        e = random.randint(-5, 5)*2
    f = 0
    while f == 0:
        f = random.randint(-5, 5)*2
    g = 0
    while g == 0:
        g = random.randint(-5, 5)*2
    #Kiểm tra e,f,g để rút gọn còn lại thì trả giá trị cũ
    if (e % 2 == 0 and f % 2 == 0 and g % 2 == 0):
        e = e//2
        f = f//2
        g = g//2
    
    
    #Đáp Án Trắc Nghiệm
        choice_0 = f'({-e};{-f};{-g})'
        choice_1 = f'({-e};{-f};{g})'
        choice_2 = f'({e};{-f};{-g})'
        choice_3 = f'({-e};{f};{-g})'
    
    # Các phương án choice_0, choice_1, choice_2, choice_3
    options = [choice_0, choice_1, choice_2, choice_3]

    # Chọn ngẫu nhiên 4 phương án trong list options
    random_options = random.sample(options, 4)

    # Thêm \True vào phương án đúng và trộn nó lại
    question = f'\\begin{{ex}} \nCho đường thẳng $d\\colon \\dfrac{{x-{a}}}{{{e}}}=\\dfrac{{y-{b}}}{{{f}}}=\\dfrac{{z-{c}}}{{{g}}}$.   Đường thẳng  $d$  có một véctơ chỉ phương là\n \\choice\n'
    for i, option in enumerate(random_options):
        if option == choice_0:
            question += f"{{ \\True ${option}$ }}\n"
        else:
            question += f"{{ ${option}$ }}\n"
    question += ' \\end{ex}\n'

    # Làm đẹp câu hỏi
    question = question.replace('\\frac', '\\dfrac').replace('--', '+').replace('-+', '-').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x').replace('1x', 'x').replace('1y', 'y').replace('1choice', 'choice').replace('0x', ' ')
    question = replace_choiceeros(question)
    # xử lý cộng đầu dòng
    question = question.replace('$(P)\colon  +', '$(P)\colon ')
    # Lưu câu hỏi vào list exersises
    exercises.append(question)

    print(question)




#Dạng 2
print("\nDạng 2:\n")
#lập trình phép toán - khai báo biến (x-a)/e=(y-b)/f=(z-c)/g
for i in range(num_exercises):
    a, b, c  = random.sample(range(-5, 5), 3)
    #Kiểm tra  e,f,g khác không
    e = 0
    while e == 0:
        e = random.randint(-5, 5)*2
    f = 0
    while f == 0:
        f = random.randint(-5, 5)*2
    g = 0
    while g == 0:
        g = random.randint(-5, 5)*2
    
    #Kiểm tra e,f,g để rút gọn
    if e != 0 and f != 0 and g != 0 and e % 2 == 0 and f % 2 == 0 and g % 2 == 0:
        em = e//2
        fm = f//2
        gm = g//2
    
    
        #Đáp Án Trắc Nghiệm
        choice_0 = f'({em};{fm};{gm})'
        choice_1 = f'({-em};{-fm};{gm})'
        choice_2 = f'({em};{-fm};{-gm})'
        choice_3 = f'({-em};{fm};{-gm})'
    
    # Các phương án choice_0, choice_1, choice_2, choice_3
    options = [choice_0, choice_1, choice_2, choice_3]

    # Chọn ngẫu nhiên 4 phương án trong list options
    random_options = random.sample(options, 4)

    # Thêm \True vào phương án đúng và trộn nó lại
    question = f'\\begin{{ex}} \nCho đường thẳng $d\\colon \\dfrac{{x-{a}}}{{{e}}}=\\dfrac{{y-{b}}}{{{f}}}=\\dfrac{{z-{c}}}{{{g}}}$.   Tìm một véctơ chỉ phương của $d$.\n \\choice\n'
    for i, option in enumerate(random_options):
        if option == choice_0:
            question += f"{{ \\True ${option}$ }}\n"
        else:
            question += f"{{ ${option}$ }}\n"
    question += ' \\end{ex}\n'

    # Làm đẹp câu hỏi
    question = question.replace('\\frac', '\\dfrac').replace('--', '+').replace('-+', '-').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x').replace('1x', 'x').replace('1y', 'y').replace('1choice', 'choice').replace('0x', ' ')
    question = replace_choiceeros(question)
    # xử lý cộng đầu dòng
    question = question.replace('$(P)\colon  +', '$(P)\colon ')
    # Lưu câu hỏi vào list exersises
    exercises.append(question)

    print(question)


#Dạng 3: chia hết cho 3

print("\nDạng 3:\n")
#lập trình phép toán - khai báo biến (x-a)/e=(y-b)/f=(z-c)/g
for i in range(num_exercises):
    a, b, c  = random.sample(range(-5, 5), 3)
    #Kiểm tra  e,f,g khác không
    e = 0
    while e == 0:
        e = random.randint(-5, 5)*3
    f = 0
    while f == 0:
        f = random.randint(-5, 5)*3
    g = 0
    while g == 0:
        g = random.randint(-5, 5)*3
    
    #Kiểm tra e,f,g để rút gọn
    if e != 0 and f != 0 and g != 0 and e % 3 == 0 and f % 3 == 0 and g % 3 == 0:
        em = e//3
        fm = f//3
        gm = g//3
    
    
        #Đáp Án Trắc Nghiệm
        choice_0 = f'({em};{fm};{gm})'
        choice_1 = f'({-em};{-fm};{gm})'
        choice_2 = f'({em};{-fm};{-gm})'
        choice_3 = f'({-em};{fm};{-gm})'
    
    # Các phương án choice_0, choice_1, choice_2, choice_3
    options = [choice_0, choice_1, choice_2, choice_3]

    # Chọn ngẫu nhiên 4 phương án trong list options
    random_options = random.sample(options, 4)

    # Thêm \True vào phương án đúng và trộn nó lại
    question = f'\\begin{{ex}} \nCho đường thẳng $d\\colon \\dfrac{{x-{a}}}{{{e}}}=\\dfrac{{y-{b}}}{{{f}}}=\\dfrac{{z-{c}}}{{{g}}}$.   Đường thẳng  $d$  có một véctơ chỉ phương là\n \\choice\n'
    for i, option in enumerate(random_options):
        if option == choice_0:
            question += f"{{ \\True ${option}$ }}\n"
        else:
            question += f"{{ ${option}$ }}\n"
    question += ' \\end{ex}\n'

    # Làm đẹp câu hỏi
    question = question.replace('\\frac', '\\dfrac').replace('--', '+').replace('-+', '-').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x').replace('1x', 'x').replace('1y', 'y').replace('1choice', 'choice').replace('0x', ' ')
    question = replace_choiceeros(question)
    # xử lý cộng đầu dòng
    question = question.replace('$(P)\colon  +', '$(P)\colon ')
    # Lưu câu hỏi vào list exersises
    exercises.append(question)

    print(question)


# Đường dẫn đến thư mục chứa file "khoangcach1diem.tex"
folder_path = "D:/DAY ONLINE/MAIN ONLINE 12/data/"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
# Tên file để lưu bài tập
file_name = "12-ptdt-oxyz-Dang-docVTCP.tex"

# Đường dẫn đầy đủ đến file bài tập
file_path = os.path.join(folder_path, file_name)

# Ghi các bài tập vào file
with open(file_path, "w", encoding="utf-8") as f:
    for i, exercise in enumerate(exercises):
        f.write(f"%Exercise {i+1}:\n{exercise}\n\n")
    
print(f"Đã lưu bài tập vào file {file_path}\n \\input{{data/{file_name}}}")
# Mở thư mục
subprocess.Popen(f'explorer {os.path.realpath(folder_path)}')


#Dạng 4: chia hết cho 5

print("\nDạng 4:\n")
#lập trình phép toán - khai báo biến (x-a)/e=(y-b)/f=(z-c)/g
for i in range(num_exercises):
    a, b, c  = random.sample(range(-5, 5), 3)
    #Kiểm tra  e,f,g khác không
    e = 0
    while e == 0:
        e = random.randint(-5, 5)*5
    f = 0
    while f == 0:
        f = random.randint(-5, 5)*5
    g = 0
    while g == 0:
        g = random.randint(-5, 5)*5
    
    #Kiểm tra e,f,g để rút gọn
    if e != 0 and f != 0 and g != 0 and e % 5 == 0 and f % 5 == 0 and g % 5 == 0:
        em = e//5
        fm = f//5
        gm = g//5
    
    
        #Đáp Án Trắc Nghiệm
        choice_0 = f'({em};{fm};{gm})'
        choice_1 = f'({-em};{-fm};{gm})'
        choice_2 = f'({em};{-fm};{-gm})'
        choice_3 = f'({-em};{fm};{-gm})'
    
    # Các phương án choice_0, choice_1, choice_2, choice_3
    options = [choice_0, choice_1, choice_2, choice_3]

    # Chọn ngẫu nhiên 4 phương án trong list options
    random_options = random.sample(options, 4)

    # Thêm \True vào phương án đúng và trộn nó lại
    question = f'\\begin{{ex}} \nCho đường thẳng $d\\colon \\dfrac{{x-{a}}}{{{e}}}=\\dfrac{{y-{b}}}{{{f}}}=\\dfrac{{z-{c}}}{{{g}}}$.   Tìm một véctơ chỉ phương của $d$.\n \\choice\n'
    for i, option in enumerate(random_options):
        if option == choice_0:
            question += f"{{ \\True ${option}$ }}\n"
        else:
            question += f"{{ ${option}$ }}\n"
    question += ' \\end{ex}\n'

    # Làm đẹp câu hỏi
    question = question.replace('\\frac', '\\dfrac').replace('--', '+').replace('-+', '-').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x').replace('1x', 'x').replace('1y', 'y').replace('1choice', 'choice').replace('0x', ' ')
    question = replace_choiceeros(question)
    # xử lý cộng đầu dòng
    question = question.replace('$(P)\colon  +', '$(P)\colon ')
    # Lưu câu hỏi vào list exersises
    exercises.append(question)

    print(question)


# Đường dẫn đến thư mục chứa file "khoangcach1diem.tex"
folder_path = "D:/DAY ONLINE/MAIN ONLINE 12/data/"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
# Tên file để lưu bài tập
file_name = "12-ptdt-oxyz-Dang-docVTCP.tex"

# Đường dẫn đầy đủ đến file bài tập
file_path = os.path.join(folder_path, file_name)

# Ghi các bài tập vào file
with open(file_path, "w", encoding="utf-8") as f:
    for i, exercise in enumerate(exercises):
        f.write(f"%Exercise {i+1}:\n{exercise}\n\n")
    
print(f"Đã lưu bài tập vào file {file_path}\n \\input{{data/{file_name}}}")
# Mở thư mục
subprocess.Popen(f'explorer {os.path.realpath(folder_path)}')



#Dạng 4.1: chia hết cho -5

print("\nDạng 4:\n")
#lập trình phép toán - khai báo biến (x-a)/e=(y-b)/f=(z-c)/g
for i in range(num_exercises):
    a, b, c  = random.sample(range(-5, 5), 3)
    #Kiểm tra  e,f,g khác không
    e = 0
    while e == 0:
        e = random.randint(-5, 5)*5
    f = 0
    while f == 0:
        f = random.randint(-5, 5)*5
    g = 0
    while g == 0:
        g = random.randint(-5, 5)*5
    
    #Kiểm tra e,f,g để rút gọn
    if e != 0 and f != 0 and g != 0 and e % 5 == 0 and f % 5 == 0 and g % 5 == 0:
        em = e//5
        fm = f//5
        gm = g//5
    
    
        #Đáp Án Trắc Nghiệm
        choice_0 = f'({-em};{-fm};{-gm})'
        choice_1 = f'({-em};{-fm};{gm})'
        choice_2 = f'({em};{-fm};{-gm})'
        choice_3 = f'({-em};{fm};{-gm})'
    
    # Các phương án choice_0, choice_1, choice_2, choice_3
    options = [choice_0, choice_1, choice_2, choice_3]

    # Chọn ngẫu nhiên 4 phương án trong list options
    random_options = random.sample(options, 4)

    # Thêm \True vào phương án đúng và trộn nó lại
    question = f'\\begin{{ex}} \nCho đường thẳng $d\\colon \\dfrac{{x-{a}}}{{{e}}}=\\dfrac{{y-{b}}}{{{f}}}=\\dfrac{{z-{c}}}{{{g}}}$.   Tìm một véctơ chỉ phương của $d$.\n \\choice\n'
    for i, option in enumerate(random_options):
        if option == choice_0:
            question += f"{{ \\True ${option}$ }}\n"
        else:
            question += f"{{ ${option}$ }}\n"
    question += ' \\end{ex}\n'

    # Làm đẹp câu hỏi
    question = question.replace('\\frac', '\\dfrac').replace('--', '+').replace('-+', '-').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x').replace('1x', 'x').replace('1y', 'y').replace('1choice', 'choice').replace('0x', ' ')
    question = replace_choiceeros(question)
    # xử lý cộng đầu dòng
    question = question.replace('$(P)\colon  +', '$(P)\colon ')
    # Lưu câu hỏi vào list exersises
    exercises.append(question)

    print(question)


# Đường dẫn đến thư mục chứa file "khoangcach1diem.tex"
folder_path = "D:/DAY ONLINE/MAIN ONLINE 12/data/"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
# Tên file để lưu bài tập
file_name = "12-ptdt-oxyz-Dang-docVTCP.tex"

# Đường dẫn đầy đủ đến file bài tập
file_path = os.path.join(folder_path, file_name)

# Ghi các bài tập vào file
with open(file_path, "w", encoding="utf-8") as f:
    for i, exercise in enumerate(exercises):
        f.write(f"%Exercise {i+1}:\n{exercise}\n\n")
    
print(f"Đã lưu bài tập vào file {file_path}\n \\input{{data/{file_name}}}")
# Mở thư mục
subprocess.Popen(f'explorer {os.path.realpath(folder_path)}')