# BÀI TẬP 1
# tính tổng bình phương 
x=2
def tong_binh_phuong(x):
    tong = 0
    for i in range(1 , x+1):
        tong += i**2
    return tong

print(tong_binh_phuong(x))

# tính tổng lap phương 

def tong_lap_phuong(x):
    tong = 0
    for i in range(1 , x+1):
        tong += i**3
    return tong

print(tong_lap_phuong(x))