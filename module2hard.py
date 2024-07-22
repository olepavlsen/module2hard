n = int(input('Введите число от 3 до 20: '))
divisors = []
parole = []
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
divisors.remove(1)
if 2 in divisors:
    divisors.remove(2)
for j in range(len(divisors)):
    parole.append(1)
    parole.append(divisors[j] - 1)
for k in range(len(divisors)):
    if divisors[k] - 2 > 2:
        parole.append(2)
        parole.append(divisors[k] - 2)
for lk in range(len(divisors)):
    if divisors[lk] - 3 > 3:
        parole.append(3)
        parole.append(divisors[lk] - 3)
for m in range(len(divisors)):
    if divisors[m] - 4 > 4:
        parole.append(4)
        parole.append(divisors[m] - 4)
for n in range(len(divisors)):
    if divisors[n] - 5 > 5:
        parole.append(5)
        parole.append(divisors[n] - 5)
for o in range(len(divisors)):
    if divisors[o] - 6 > 6:
        parole.append(6)
        parole.append(divisors[o] - 6)
for p in range(len(divisors)):
    if divisors[p] - 7 > 7:
        parole.append(7)
        parole.append(divisors[p] - 7)
for q in range(len(divisors)):
    if divisors[q] - 8 > 8:
        parole.append(8)
        parole.append(divisors[q] - 8)
for r in range(len(divisors)):
    if divisors[r] - 9 > 9:
        parole.append(9)
        parole.append(divisors[r] - 9)
print('Пароль: ', str(parole)[1:-1].replace(", ", ""))
