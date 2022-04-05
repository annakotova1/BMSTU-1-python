# Данные для подсчета:
# 0,1 - отрезок разбиения,
# 2 - шаг,
# 3 - точность(0 - какую eps использовать ('1','2', '12'), eps1, eps2)
# 4 - максимальное кол-во иттераций

tabl = '|{}|{}|{}|{}|{}|{}|{}|{}|'


def output_results(results, len_strings):
    shapka_start = ['Н.', 'Левая', 'Правая', 'Значение', 'Значение', 'Реальное ч.', 'Код', 'Время']
    ss1, ss2, ss3, ss4, ss5, ss6, ss7, ss8 = shapka_start
    shapka_finish = ['', 'гран.', 'гран.', 'корня', 'функции', 'иттераций', 'ош.', '']
    sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8 = shapka_finish
    shapka = '|{:^3}|{:^7}|{:^7}|{:^10}|{:^10}|{:^11}|{:^4}|{:^10}|'
    tabl = '|{:^3}|{:>5.2f}  |{:>5.2f}  |{:10.6f}|{:10.6f}|{:^11}|{:^4}|{:10.9f}|'
    print(shapka.format(ss1, ss2, ss3, ss4, ss5, ss6, ss7, ss8))
    print(shapka.format(sf1, sf2, sf3, sf4, sf5, sf6, sf7, sf8))
    print('_' * len(tabl))
    print()
    for i in range(len(results)):
        a = results[i][0]
        b = results[i][1]
        c = results[i][2]
        d1 = results[i][3][0]
        d2 = results[i][3][1]
        e1 = results[i][4][0]
        e2 = results[i][4][1]
        f1 = results[i][5][0]
        f2 = results[i][5][1]
        g1 = results[i][6][0]
        g2 = results[i][6][1]
        print(tabl.format(a, b, c, d1, e1, f1, g1, 0))
        print(tabl.format(0, 0, 0, d2, e2, f2, g2, 0))
        print('_'*len(tabl))
        print()


