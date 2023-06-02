import datetime


def get_birthdays_per_week(users):
    today = datetime.date.today()
    current_week_start = today - datetime.timedelta(days=today.weekday())
    current_week_end = current_week_start + datetime.timedelta(days=6)

    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    birthday_dict = {}

    for user in users:
        name = user['name']
        birthday = user['birthday'].date()

        if current_week_start <= birthday <= current_week_end:
            weekday = weekdays[birthday.weekday()]

            if weekday in birthday_dict:
                birthday_dict[weekday].append(name)
            else:
                birthday_dict[weekday] = [name]

    for weekday, names in birthday_dict.items():
        print(f"{weekday}: {', '.join(names)}")
