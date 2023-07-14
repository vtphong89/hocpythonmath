# Tìm hàm tính số chữ số của 1 số

def tim_so_chu_so(m): 
    n = 0
    while 10**n <= m:
        n=n+1
    return n

m=12.3
print(tim_so_chu_so(m))