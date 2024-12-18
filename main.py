from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    # Словник для збереження днів народження по днях тижня
    birthdays = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

    # Отримуємо сьогоднішню дату
    today = date.today()
    current_weekday = today.weekday()

    # Обчислюємо межі наступного тижня
    start_of_week = today - timedelta(days=current_weekday)
    end_of_next_week = start_of_week + timedelta(days=13)

    # Перебираємо список користувачів
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        # Оновлюємо рік дня народження до поточного
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув, переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Перевіряємо, чи день народження у межах наступного тижня
        if today <= birthday_this_year <= end_of_next_week:
            birthday_weekday = birthday_this_year.weekday()

            # Якщо день народження у вихідні, переносимо на понеділок
            if birthday_weekday in (5, 6):
                day_name = "Monday"
            else:
                day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][birthday_weekday]

            birthdays[day_name].append(name)

    return {day: names for day, names in birthdays.items() if names}


if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Elon Musk", "birthday": datetime(1971, 6, 28).date()},
    ]

    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, names in result.items():
        if names:
            print(f"{day_name}: {', '.join(names)}")
