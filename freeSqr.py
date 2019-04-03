"""Число n свободно от квадратов тогда и только тогда, 
когда для любого его разложения на множители n = ab,
множители a и b взаимно просты"""

# Функция определяет, являются ли 2 числа простыми
def isMutuallySimple(a: int, b: int) -> bool:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    if a == 1:
        return True
    else:
        return False

# Берет простые множители
def getPrimalMultipliers(number):
    i = 2
    primalLst = []
    while i*i <= number:
        while number%i == 0:
            primalLst.append(int(i))
            number = number/i
        i += 1
    if number > 1:
        primalLst.append(int(number))
    if len(primalLst) == 2:
        return primalLst
    else:
        lst = list(set(primalLst))
        return lst

# Является ли число свободным от квадратов
def isFreeSqr(n):
    lst = getPrimalMultipliers(n)
    if isMutuallySimple(lst[0], lst[1]):
        return True
    else:
        return False

print(isFreeSqr(10))
print(isFreeSqr(4))

