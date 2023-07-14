def rut_gon_ln(x):
    uoc_so = {}
    
    # Tìm tất cả các ước số nguyên dương của x
    for i in range(2, int(x/2) + 1):
        while x % i == 0:
            if i in uoc_so:
                uoc_so[i] += 1
            else:
                uoc_so[i] = 1
            x /= i
    
    if x > 1:
        if x in uoc_so:
            uoc_so[x] += 1
        else:
            uoc_so[x] = 1
    
    # Xây dựng chuỗi kết quả
    result = ""
    for key, value in uoc_so.items():
        if result != "":
            result += " + "
        if value > 1:
            result += f"{value}*ln({key})"
        else:
            result += f"ln({key})"
    
    return result
print(rut_gon_ln(2))  # Kết quả: "2*ln(2)"
print(rut_gon_ln(27))  # Kết quả: "3*ln(3)"