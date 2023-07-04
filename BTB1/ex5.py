import random

# Hoành độ tâm
def hoanh_do_tam(a):
    if a == 0:
        return "x^2"
    if a < 0:
        return "(x " + str(a) + ")^2  "
    if a > 0:
        return "(x + " + str(a) + ")^2 "

# Tung độ tâm
def tung_do_tam(a):
    if a == 0:
        return "y^2"
    if a < 0:
        return "(y " + str(a) + ")^2"
    if a > 0:
        return "(y + " + str(a) + ")^2"

# Số bài
sobai = 100

# chọn ngẫu nhiên hệ số và tạo đáp án 
debai = ""
for i in range(1, sobai + 1):
    a = random.choice(range(-7, 7))
    b = random.choice(range(-7, 7))
    c = random.choice(range(-7, 7))
    while c == 0:
        c = random.choice(range(-7, 7))
    c = c ** 2
    
    # Đáp án trắc nghiệm
    D_A = f"I({-a}, {-b})"
    D_B = f"I({a}, {b})"
    D_C = f"I({-b}, {a})"
    D_D = f"I({b}, {-a})"
    
    # Các phương án theo list để trộn
    choices = [D_A, D_B, D_C, D_D]
    
    # Chọn ngẫu nhiên 4 phương án trong list choices
    random_choices = random.sample(choices, 4)
    # Đề bài
    debai += f"\\begin{{ex}}\nTrong mặt phẳng $Oxy$, cho phương trình đường tròn ${hoanh_do_tam(a)} + {tung_do_tam(b)} = {c}$. Tọa độ tâm của đường tròn là\n\\choice\n"
    # Thêm \True vào phương án đúng và trộn nó lại
    options = []
    for choice in random_choices:
        if choice == D_A:
            debai += f"{{ \\True ${choice}$ }}\n"
        else:
            debai += f"{{ ${choice}$ }}\n"
    debai += "  ".join(options) + "\\end{ex}\n\n"
with open("phuongtrinhduongtron.tex", mode="w", encoding="utf-8") as fileout:
    fileout.write(debai + "\n")
print(debai)
