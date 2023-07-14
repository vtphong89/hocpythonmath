#kiem tra so chính phương

def chinh_phuong(n):
    i=0
    while i**2 <n:
        i +=1
    if n == i**2:
        return "Là số chính phương"
    if n != i**2:
        return "Không là số chính phương"


n=15
print(chinh_phuong(n))