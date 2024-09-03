stroka = 'stroka' + 'ebat eto toge stroka' + 'ebat oni vmeste 123 !@#$%^&*('
stroka_s_peremennoy = 'pause ' + stroka + ' final'

print(stroka_s_peremennoy)

ciferki_1 = 1
ciferki_mnogo = 666
summa = ciferki_1 + ciferki_mnogo

print(summa)

spisok = ['stroka ', 555, ' stroka2*']
print(spisok[0] + spisok[2])
print(spisok)

# dict = { key: value } - демонстрация
slovar = {
            'vasia': 1000,
            'petia': 500
                        }
print(slovar['vasia'] + slovar['petia'])

slovar_slojniy = {
    'Vasiliy': [1000, 2000, 'nihuya'],
    'Petr': {
        'sveta': 1000,
        'galia': [5, 2]
              }
}

print(slovar_slojniy['Petr']['galia'][0])

nihuya = '1' # если в переменной есть хоть что-то, она True
nihuya_nastoyashiy = None

if nihuya: #работает полностью эквивалентно if nihuya == True
    print('nihuya est')

if nihuya_nastoyashiy:
    print('EBAT ono rabotaet')
else:
    print('ну тут и правда нихуя')
