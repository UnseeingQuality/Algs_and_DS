# Назовем натуральное число честно четным, если все цифры в его десятичной записи четные.
# Например, числа 4826 и 8802 - честно четные, а 79 и 301 - нет.

num = int(input())
is_odd = 0
while num > 0 and (not is_odd):
    dig = num % 10
    num //= 10
    if dig % 2 == 1:
        is_odd = True

if is_odd:
    print(0)
else:
    print(1)