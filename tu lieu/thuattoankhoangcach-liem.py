import sympy
import re
import random

num_exercises = 10

def replace_zeros(expression):
    pattern = r'(\+|-)0(\d*[xyz](\^\d+)?)?'
    return re.sub(pattern, ' ', expression)

for i in range(num_exercises):
    a, b, c, d, e, f, g = random.sample(range(-3, 4), 7)
    numerator = abs(d*a + e*b + f*c + g)
    denominator = sympy.sqrt(d**2 + e**2 + f**2)
    
    while numerator == 0:
        a, b, c, d, e, f, g = random.sample(range(-3, 4), 7)
        numerator = abs(d*a + e*b + f*c + g)
        denominator = sympy.sqrt(d**2 + e**2 + f**2)

    x = numerator / denominator
    y = sympy.simplify(x)
    z = sympy.latex(y)
    z_1 = sympy.latex(y / 2)
    z_2 = sympy.latex(y / 3)
    z_3 = sympy.latex(2 * y)
    
    debai = f'\\begin{{ex}} \nTrong không gian với hệ tọa độ $Oxyz$, cho mặt phẳng $(P): {d}x+{e}y+{f}z+{g}=0$ và điểm $M({a};{b};{c})$. Tính khoảng cách $d$ từ $M$ đến $(P)$.\n \\choice\n {{${z}$}}\n{{${z_1}$}}\n{{${z_2}$}}\n{{${z_3}$}}\n \\end{{ex}}'

    debai = debai.replace('\\frac', '\\dfrac').replace('+-', '-').replace('-1x', '-x').replace('+1x', '+x').replace('1x', 'x').replace('1y', 'y').replace('1z', 'z').replace('0x', ' ')
    debai = replace_zeros(debai)
    
    print(f"Exercise {i+1}:\n{debai}\n") 
