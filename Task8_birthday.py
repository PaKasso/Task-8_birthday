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
        birthday = user['birthday']

        if current_week_start.month == birthday.month and current_week_start.day <= birthday.day <= current_week_end.day:
            weekday = weekdays[birthday.weekday()]

            if weekday in birthday_dict:
                birthday_dict[weekday].append((name, birthday))
            else:
                birthday_dict[weekday] = [(name, birthday)]

    return birthday_dict


users = [
    {'name': 'Bill', 'birthday': datetime.date(1991, 6, 6)},
    {'name': 'Jill', 'birthday': datetime.date(1992, 6, 9)},
    {'name': 'Kim', 'birthday': datetime.date(1985, 6, 8)},
    {'name': 'Jan', 'birthday': datetime.date(1995, 6, 6)}
]

birthdays = get_birthdays_per_week(users)


for weekday, entries in birthdays.items():
    print(f"{weekday}:")
    for name, birthday in entries:
        print(f"  {name} - {birthday.strftime('%Y-%m-%d')}")
