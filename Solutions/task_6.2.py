user_val = str(input('Enter your number from 0 to 864000: '))
day_num = 24 * 3600
hours_num = 3600
minutes_num = 60

if user_val.isdigit():
    user_val = int(user_val)
    if not 0 <= user_val <= 864000:
        print('Bro, I`m sorry, but your your entered data is invalid :(', 'Please, try Again! :) ', sep='\n')
    else:
        # рахуємо наші дані, які нам будуть потрібні потім
        days_val, hours_none = divmod(user_val, day_num)
        hours_val, minutes_none = divmod(hours_none, hours_num)
        minutes_val, second_none = divmod(minutes_none, minutes_num)

        # заганяємо назад в стрінгу, щоб додавати нулі, в разі потреби
        day = str(days_val).zfill(1)
        hours = str(hours_val).zfill(2)
        minutes = str(minutes_val).zfill(2)
        second = str(second_none).zfill(2)
        # Прінтимо наші результати
        print(f'{day} days, {hours}:{minutes}:{second}')
else:
    print('Bro, I`m sorry, but your your entered data contains text.', 'Please, try Again! :) ', sep='\n')




# P.S
# Дуже хотілося засунути всі перетворення в прінт, але не став гольфити))