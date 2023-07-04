import random

# hệ số a
def hesoa(a):
    if a == 1:
        return "x^2"
    if a == -1:
        return "-x^2"
    if a > 0:
        return str(a) + "x^2"
    if a == 0:
        return ""
    if a < 0:
        return str(a) + "x^2"

# hệ số b
def hesob(a):
    if a == 1:
        return "+" + "x"
    if a == -1:
        return "-x"
    if a > 0:
        return "+" + str(a) + "x"
    if a == 0:
        return ""
    if a < 0:
        return str(a) + "x"

# hệ số c
def hesoc(a):
    if a > 0:
        return "+" + str(a)
    if a == 0:
        return ""
    if a < 0:
        return str(a)

# số bài in ra
sobai = 100

# random hệ số và ghi vào file
with open("tamthucbachai.tex", mode="w", encoding="utf-8") as fileout:
    for i in range(1, sobai + 1):
        a = random.choice(range(-5, 6))
        while a == 0:
            a = random.choice(range(-5, 6))
        b = random.choice(range(-5, 6))
        c = random.choice(range(-5, 6))
        debai = "$$y=" + hesoa(a) + hesob(b) + hesoc(c) + "$$"
        fileout.write(debai + "\n")
        print(debai)
