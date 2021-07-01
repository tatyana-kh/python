sec_in = int(input('Введите время в секундах: '))
min_calc = sec_in / 60
hour = int(min_calc // 60)
sec_calc = sec_in % 3600
min = sec_calc // 60
sec = sec_calc % 60
print(f"{sec_in} секунд это: {hour} ч {min} мин {sec} сек")
