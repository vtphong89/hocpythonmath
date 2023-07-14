
n = 32
# Kiểm tra một số có là lập phương hay không
def kiem_tra_lap_phuong(n):
    i = 0
    while i ** 3 < n:
        i += 1
    if i ** 3 == n:
        return True
    else:
        return False

# Tìm ước lớn nhất có lập phương sử dụng list
def uoc_lap_phuong_max(n):
    uoc = []
    for i in range(1, n + 1):
        if n % i == 0 and kiem_tra_lap_phuong(i) == True:
            uoc.append(i)
    return max(uoc)

# Tìm căn lập phương
def can_lap_phuong(n):
    i = 0
    while i ** 3 < n:
        i += 1
    if  i ** 3 == n:
        return i
    else:
        None

# Tìm căn bậc ba
def can_bac_ba(n):
    a = can_lap_phuong(uoc_lap_phuong_max(n))
    b = int(n/uoc_lap_phuong_max(n))
    if a == 1:
        if b ==1:
            return "1"
        else:
            return "\\sqrt[3]{"+str(b)+"}"
    else:
        if b == 1:
            return str(a)
        else:
            return str(a) + "\\sqrt[3]{"+str(b) + "}"
        
print(can_bac_ba(n))