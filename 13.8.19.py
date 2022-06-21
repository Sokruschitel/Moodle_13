N=int(input('Введите колличество билетов'))
S=0
for i in range(1, N+1):
    w=int(input('Введите возраст'))
    if w<18:
        S=S
    elif 18<=w<=25:
        S=S+990
    else:
        S=S+1390
if N>=3:
    S=S*0.9
    print("Стоимость с учетом скидки",S)
else:
    print('Стоимость',S)
