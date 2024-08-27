import datetime

# Функция для запроса даты рождения у пользователя
def get_birthday():
    day = int(input("Введите день вашего рождения (дд): "))
    month = int(input("Введите месяц вашего рождения (мм): "))
    year = int(input("Введите год вашего рождения (гггг): "))
    return datetime.date(year, month, day)

# Функция для определения дня недели
def get_weekday(birthday):
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days[birthday.weekday()]

# Функция для определения високосного года
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Функция для определения возраста пользователя
def calculate_age(birthday):
    today = datetime.date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

# Функция для прорисовки цифр звёздочками
def draw_digit(digit):
    digits = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "*   *", "   * ", "  *  ", "*****"],
        '3': [" *** ", "    *", " *** ", "    *", " *** "],
        '4': ["   * ", "  ** ", " * * ", "*****", "   * "],
        '5': ["*****", "*    ", "**** ", "    *", " *** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "    *", "   * ", "  *  ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "]
    }
    return digits[digit]

# Функция для прорисовки всей даты
def draw_date(day, month, year):
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"
    year_str = f"{year:04d}"
    full_date = day_str + month_str + year_str

    lines = ["", "", "", "", ""]
    for digit in full_date:
        digit_lines = draw_digit(digit)
        for i in range(5):
            lines[i] += digit_lines[i] + "  "

    for line in lines:
        print(line)

# Основная часть программы
birthday = get_birthday()

# Определение дня недели
weekday = get_weekday(birthday)
print(f"Вы родились в {weekday}.")

# Проверка на високосный год
leap_year = is_leap_year(birthday.year)
if leap_year:
    print(f"{birthday.year} год был високосным.")
else:
    print(f"{birthday.year} год не был високосным.")

# Определение возраста
age = calculate_age(birthday)
print(f"Вам сейчас {age} лет.")

# Прорисовка даты рождения
print("Ваша дата рождения:")
draw_date(birthday.day, birthday.month, birthday.year)