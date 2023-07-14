import random

so_cau = 10

bt_cau_hoi_hai = "Bài 1. Rút gọn:\\\\\n"
numbers = []
i = 0

while i < so_cau:
    a = random.choice(range(1, 100))
    if a % 4 == 0 and a not in numbers:
        numbers.append(a)
        bt_cau_hoi_hai = bt_cau_hoi_hai + str(i + 1) + ")" + "$\\sqrt{" + str(a) + "}$\\\\\n"
        i += 1
print(bt_cau_hoi_hai)

bt_cau_hoi_ba = "Bài 2. Rút gọn:\\\\\n"
numbers = []
i = 0
while i < so_cau:
    a = random.choice(range(1, 100))
    if a % 9 == 0 and a not in numbers:
        numbers.append(a)
        bt_cau_hoi_ba = bt_cau_hoi_ba + str(i + 1) + ")" + "$\\sqrt{" + str(a) + "}$\\\\\n"
        i += 1

print(bt_cau_hoi_ba)


bt_cau_hoi_bon = "Bài 3. Rút gọn:\\\\\n"
numbers = []
i = 0
while i < so_cau:
    a = random.choice(range(1, 200))
    if a % 16 == 0 and a not in numbers:
        numbers.append(a)
        bt_cau_hoi_bon = bt_cau_hoi_bon + str(i + 1) + ")" + "$\\sqrt{" + str(a) + "}$\\\\\n"
        i += 1

print(bt_cau_hoi_bon)

bt_cau_hoi_nam = "Bài 4. Rút gọn:\\\\\n"
numbers = []
i = 0
while i < so_cau:
    a = random.choice(range(1, 1000))
    if a % 25 == 0 and a not in numbers:
        numbers.append(a)
        bt_cau_hoi_nam = bt_cau_hoi_nam + str(i + 1) + ")" + "$\\sqrt{" + str(a) + "}$\\\\\n"
        i += 1

print(bt_cau_hoi_nam)