"""Дано символи s1, s2, .... Відомо, що символ s1 відмінний від пробілу і що серед s2,
s3, ... є хоча б один пробіл. Розглядаються s1, ..., sn - символи, що передують першому
пробілу (n заздалегідь не відомо). Перетворити послідовність s1, ..., sn, видаливши з неї
всі символи, які не є буквами."""
while True:
    import string

    symbols_set = set()
    symbols_list = []
    nomer = 1
    while " " not in symbols_set:
        symbol = input(f'Введіть s{nomer} символ:  ')
        nomer = nomer + 1
        symbols_set.add(symbol)
        symbols_list.append(symbol)
    print(symbols_list)
    update_symbols = [symbol for symbol in symbols_list if
                      symbol not in string.digits and symbol not in string.punctuation]
    for i in update_symbols:
        print(i, end=' ')
    print(f'If you want to exit {exit}')
    leave = input()
    if leave == 'exit':
        break
