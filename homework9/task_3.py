# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
sum_buy = []
cur_buy = 0
with open("test_file/task_3.txt", 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if line[:-1].isdigit():
            cur_buy += int(line)
        else:
            sum_buy.append(cur_buy)
            cur_buy = 0
    sum_buy.append(cur_buy)
sort_sum_buy = sorted(sum_buy, reverse=True)
three_most_expensive_purchases = sum(sort_sum_buy[:3])

assert three_most_expensive_purchases == 202346
