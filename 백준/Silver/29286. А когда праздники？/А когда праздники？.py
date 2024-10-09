import calendar

# Названия дней недели и месяцев в нужном порядке
days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
months_of_year = ['january', 'february', 'march', 'april', 'may', 'june', 
                  'july', 'august', 'september', 'october', 'november', 'december']

# Функция для поиска нужного дня
def find_day(first_day_of_year, is_leap, holiday):
    first_or_last, day, _, month = holiday.split()
    month_index = months_of_year.index(month) + 1
    day_index = days_of_week.index(day)

    # Получаем количество дней в месяце с учётом високосного года
    if month == 'february' and is_leap == 'yes':
        days_in_month = 29
    else:
        days_in_month = calendar.monthrange(2020 if is_leap == 'yes' else 2021, month_index)[1]

    # Найдём номер дня недели для 1-го числа данного месяца
    first_day_of_month = (first_day_of_year + sum(calendar.monthrange(2020 if is_leap == 'yes' else 2021, i + 1)[1] for i in range(month_index - 1))) % 7
    
    # Если ищем первый указанный день недели
    if first_or_last == 'first':
        for day_num in range(1, days_in_month + 1):
            if (first_day_of_month + day_num - 1) % 7 == day_index:
                return day_num

    # Если ищем последний указанный день недели
    elif first_or_last == 'last':
        for day_num in range(days_in_month, 0, -1):
            if (first_day_of_month + day_num - 1) % 7 == day_index:
                return day_num

def solve():
    # Ввод
    n = int(input())
    first_day_of_year, is_leap = input().split()
    holidays = [input().strip() for _ in range(n)]

    # Определяем первый день года
    first_day_of_year_index = days_of_week.index(first_day_of_year)

    # Для каждого праздника находим дату
    for holiday in holidays:
        result = find_day(first_day_of_year_index, is_leap, holiday)
        print(result)

solve()