from datetime import datetime, timedelta, date
import calendar

def get_birthdays_per_week(users):
    # Отримуємо сьогоднішній день
    
    today = date.today()
    
    # Створюємо словник із ключами днів тижня 
    weekdays = {day: [] for day in calendar.day_name}
    
    
    for user in users:
        # День народження цього року
        birth_this_year = user['birthday'].replace(year=today.year)
        
        # День народження наступного року
        birth_next_year = user['birthday'].replace(year=today.year + 1)
        
        # Список днів народжень, які треба врахувати
        upcoming_birthdays = []
        
        if today <= birth_this_year <= today + timedelta(days=6):
            upcoming_birthdays.append(birth_this_year)
            
        if today <= birth_next_year <= today + timedelta(days=6):
            upcoming_birthdays.append(birth_next_year)
        
        for upcoming_birthday in upcoming_birthdays:
            # Визначаємо день тижня 
            weekday = calendar.day_name[upcoming_birthday.weekday()]
            
            # Переносимо на понеділок, якщо це вихідний
            if weekday in ['Saturday', 'Sunday']:
                weekday = 'Monday'
            
            # Додаємо користувача у відпоівдний день тижня
            weekdays[weekday].append(user['name'])
    
    
    weekdays = {k: v for k, v in weekdays.items() if v}
    
    return weekdays


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")