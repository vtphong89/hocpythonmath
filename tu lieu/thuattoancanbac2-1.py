import random
from math import sqrt

x = 2

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = - a**2 + c**2
        if b > 0:
            numerator = f'\\sqrt{{x^2+{int(b)}}}-{c}'
            denominator = f'x-{a}'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = - a**2 + c**2
        if b < 0:
            numerator = f'\\sqrt{{x^2 {int(b)}}}-{c}'
            denominator = f'x-{a}'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = a**2 - c**2
        if b > 0:
            numerator = f'{c}-\\sqrt{{x^2-{int(b)}}}'
            denominator = f'x-{a}'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = -a**2 + c**2
        if b > 0:
            numerator = f'{c}-\\sqrt{{x^2+{int(b)}}}'
            denominator = f'x-{a}'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

# Đảo mẫu nhé

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = - a**2 + c**2
        if b > 0:
            numerator = f'\\sqrt{{x^2+{int(b)}}}-{c}'
            denominator = f'{a}-x'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = - a**2 + c**2
        if b < 0:
            numerator = f'\\sqrt{{x^2 {int(b)}}}-{c}'
            denominator = f'{a}-x'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = a**2 - c**2
        if b > 0:
            numerator = f'{c}-\\sqrt{{x^2-{int(b)}}}'
            denominator = f'{a}-x'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = -a**2 + c**2
        if b > 0:
            numerator = f'{c}-\\sqrt{{x^2+{int(b)}}}'
            denominator = f'{a}-x'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

# Giờ thì căn nằm dưới nhé

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = - a**2 + c**2
        if b > 0:
            numerator = f'\\sqrt{{x^2+{int(b)}}}-{c}'
            denominator = f'x-{a}'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = - a**2 + c**2
        if b < 0:
            numerator = f'\\sqrt{{x^2 {int(b)}}}-{c}'
            denominator = f'x-{a}'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = a**2 - c**2
        if b > 0:
            numerator = f'{c}-\\sqrt{{x^2-{int(b)}}}'
            denominator = f'x-{a}'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{numerator}}}{{{denominator}}}$'
            print(result_str)
            break

for i in range(x):
    while True:
        a, c = random.randint(1, 9), random.randint(1, 9)
        b = -a**2 + c**2
        if b > 0:
            numerator = f'{c}-\\sqrt{{x^2+{int(b)}}}'
            denominator = f'x-{a}'
            result_str = f'\item $\\lim\\limits_{{x \\to {a}}}\\dfrac{{{denominator}}}{{{numerator}}}$'
            print(result_str)
            break