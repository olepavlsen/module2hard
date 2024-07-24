n = int(input('Введите число от 3 до 20: '))
divisors = []
parole = []
m = 1
for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
    if 1 in divisors:
        divisors.remove(1)
    if 2 in divisors:
        divisors.remove(2)
while m <= n / 2:
    for k in range(len(divisors)):
        if divisors[k] - m > m:
            parole.append(m)
            parole.append(divisors[k] - m)
    m += 1
print('Пароль: ', str(parole)[1:-1].replace(", ", ""))
