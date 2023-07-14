def kt_cp(n):
    i = 0
    while i ** 2 < n:
        i += 1
    if n == i **2:
        return True
    else:
        return False

def uoc_cp_max(n):
    danhsach = []
    for i in range(1 , n+1):
        if n % i == 0 and kt_cp(i) == True:
            danhsach.append(i)
    return danhsach[len(danhsach)-1]
    
def can_chinh_phuong(n):
    i =0 
    while i ** 2 != n:
        i +=1
    return i

def can_bac_hai(n):
    a = can_chinh_phuong(uoc_cp_max(n))
    b = int(n/uoc_cp_max(n))
    if a == 1:
        if b ==1:
            return "1"
        else:
            return "\\sqrt{"+str(b)+"}"
    else:
        if b == 1:
            return str(a)
        else:
            return str(a) + "\\sqrt{"+str(b) + "}"
        
n = 6
print(can_bac_hai(n))