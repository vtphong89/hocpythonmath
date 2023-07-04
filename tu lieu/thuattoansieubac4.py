import random
import re

def replace_zeros(expression):
    # Tìm kiếm các chuỗi cần thay thế và thay thế bằng ' '
    pattern = r'(\+|-)0(\d*x(\^\d+)?)?'
    return re.sub(pattern, ' ', expression)
    
# Vòng lặp để thực hiện tính toán và in kết quả cho 5 set giá trị ngẫu nhiên
for i in range(5):
    # Khởi tạo các biến a, b, c, d, e, f, g với các giá trị ngẫu nhiên trong khoảng [-3, 3]
    a, b, c, d, e, f, g = [random.randint(-3, 3) for _ in range(7)]

    # Tính giá trị của các biểu thức A, B, C, D, E, F, G, H
    A = a + b + c + d
    B = a*b + a*c + a*d + b*c + b*d + c*d
    C = a*b*c + a*b*d + a*c*d + b*c*d
    D = a*b*c*d
    E = a + e + f + g
    F = a*e + a*f + a*g + e*f + e*g + f*g
    G = a*e*f + a*e*g + a*f*g + e*f*g
    H = a*e*f*g

    # Tính giá trị của biểu thức
    numerator = f'x^4 -{A}x^3 +{B}x^2 -{C}x +{D}'
    denominator = f'x^4 -{E}x^3 +{F}x^2 -{G}x +{H}'

    # Thay thế các chuỗi '--' và '+-' trong numerator và denominator bằng '-' và '+'
    numerator = numerator.replace('--', '+').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x')
    denominator = denominator.replace('--', '+').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x')
    numerator = replace_zeros(numerator)
    denominator = replace_zeros(denominator)
    # Tạo chuỗi kết quả với giá trị của i và giá trị a
    result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'

    # In kết quả
    print(result_str)