def find_smallest_number():
    n = 1
    while True:
        if n % 30 == 7 and n % 40 == 17:
            return n
        n += 1

# Gọi hàm để tìm số nhỏ nhất thỏa mãn
result = find_smallest_number()
print(result)