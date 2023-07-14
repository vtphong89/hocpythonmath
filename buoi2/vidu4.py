# Tìm số nguyên dương n nhỏ nhất sao cho n +1, 2n +1, 5n +1 là các số chính phương
def kt_chinh_phuong(n):
    i = 0
    while i**2 < n:
        i = i +1
    if n == i**2:
        return True
    else:
        return False
n = 1
while kt_chinh_phuong(n + 1) == False or kt_chinh_phuong(2*n + 1) == False or kt_chinh_phuong(5*n + 1) == False:
    n = n +1
    
print(n)
#print(kt_chinh_phuong(n))
