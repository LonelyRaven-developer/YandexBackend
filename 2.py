# Пропишите нужные импорты.
from datetime import datetime, timedelta

# Напишите код функции, следуя плану из задания.
def get_results(d1,d2):
    if d1==d2:
        print(f'Вы пробежали за {d1} и победили!')
    else:
        d1q = datetime.strptime(d1, '%H:%M:%S')
        d2q = datetime.strptime(d2, '%H:%M:%S')
        dd = d2q-d1q
        # print(dd)
        # dd = datetime.strftime(dd,'%H:%M:%S')
        print(f'Вы пробежали за {d1} с отставанием от лидера {dd}')


# Проверьте работу программы, можете подставить свои значения.
get_results('02:02:02', '02:02:02')
get_results('02:02:02', '03:04:05')
# ggd