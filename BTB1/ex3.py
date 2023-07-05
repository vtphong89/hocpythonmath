# BÀI TẬP 3.
# Tổng các số có 3 chữ số chia 4 dư 1

def sum_so_bachu_chiabon_du_mot():
    tong = 0
    for i in range(100 , 1000):
        if i % 4 == 1:
            tong += i
    return tong

print(sum_so_bachu_chiabon_du_mot())