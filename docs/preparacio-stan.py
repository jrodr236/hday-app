def suma_digits(numEntero):
    sumDigit=0
    while numEntero != 0:
        extNum = numEntero % 10
        numEntero //= 10
        sumDigit += extNum
    return sumDigit

quantitat = 0
numero = 1
while numero <= 10000:
    suma = suma_digits(numero)
    if suma%10 == 3:
        quantitat += 1
    numero += 1

print(quantitat)

