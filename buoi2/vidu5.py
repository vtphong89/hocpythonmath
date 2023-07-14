#uoc_chung_lon_nhat

def ucln(m,n):
    danhsach = []
    for i in range(1,min(m,n)+1):
        if m % i ==0 and n % i ==0:
            danhsach.append(i)
    return danhsach[len(danhsach)-1]

m = 150
n = 102
print(ucln(m,n))

def phan_so(m,n):
    a = int(m/ucln(m,n))
    b = int(n/ucln(m,n))
    if b == 1:
        return str(a)
    else:
        return "\\dfrac{" + str(a) + "}{" + str(b) +"}"

print(phan_so(m,n)) 