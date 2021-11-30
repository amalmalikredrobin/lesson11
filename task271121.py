while True:
    try:
        numOfTerms = int(input('Vvedite chislo slagaemyh: '))
        if numOfTerms < 2: raise ValueError('Chislo slagaemyh doljno byt ravno ili bolshe 2-m')
        else: break 
    except ValueError as ve:
        print(ve)

while True:
    acc = 0
    for i in range(1, numOfTerms + 1):
        num = int(input(f'Enter {i} term: '))
        acc += num
    try:
        if acc < 100: raise ValueError('Summa menshe 100')
        else:
            print(acc)
            break
    except ValueError as ve:
            print(f'Summa doljna byt bolshe 100. Pobrobuyte vvesti {numOfTerms} slagaemyh zanovo')
