# Напишите функцию to_roman, которая преобразуют арабское число (val) в римское (roman_str).
#
# Современные римские цифры записываются, выражая каждую цифру отдельно,
# начиная с самой левой цифры и пропуская цифру со значением нуля.
# Римскими цифрами 1990 отображается: 1000=М, 900=СМ, 90=ХС; в результате MCMXC.
# 2023 записывается как 2000=MM, 20=XX, 3=III; или MMXXIII.
# В 1666 используется каждый римский символ в порядке убывания: MDCLXVI.
#
# Например (Ввод --> Вывод) :
# 2008 --> MMVIII


def to_roman(val):
    """
    Преобразование арабского числа в римское
    :param val: арабское число
    :return: римское
    """
    # Здесь нужно написать код
    roman_num2 = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                  90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                  9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    # tous = val // 1000
    # hund = val // 100 % 10
    # dec = val // 10 % 10
    # ed = val % 10
    roman_str = ''

    for value, letter in roman_num2.items():
        while val >= value:
            roman_str += letter
            val -= value
    print(roman_str)
    # if tous != 0:
    #     roman_str += roman_num.get(1000) * tous
    # if hund != 0:
    #     if hund < 4:
    #         roman_str += roman_num.get(100) * hund
    #     elif hund == 4:
    #         roman_str += roman_num.get(hund * 100)
    #     elif hund < 9:
    #         roman_str += roman_num.get(500) + roman_num.get(100) * (hund % 5)
    #     else:
    #         roman_str += roman_num.get(hund * 100)
    # if dec != 0:
    #     if dec < 4:
    #         roman_str += roman_num.get(10) * dec
    #     elif dec == 4:
    #         roman_str += roman_num.get(dec * 10)
    #     elif dec < 9:
    #         roman_str += roman_num.get(50) + roman_num.get(10) * (dec % 5)
    #     else:
    #         roman_str += roman_num.get(dec * 10)
    # if ed != 0:
    #     if ed < 4:
    #         roman_str += roman_num.get(1) * ed
    #     elif ed == 4:
    #         roman_str += roman_num.get(ed)
    #     elif ed < 9:
    #         roman_str += roman_num.get(5) + roman_num.get(1) * (ed % 5)
    #     else:
    #         roman_str += roman_num.get(ed)
    return roman_str

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [1133, 2224, 1938, 1817, 2505, 391, 3743, 1634, 699, 1666, 1494, 1444]

test_data = [
    "MCXXXIII", "MMCCXXIV", "MCMXXXVIII", "MDCCCXVII", "MMDV", "CCCXCI", 'MMMDCCXLIII', 'MDCXXXIV', 'DCXCIX', 'MDCLXVI',
    'MCDXCIV', 'MCDXLIV']


for i, d in enumerate(data):
    assert to_roman(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
