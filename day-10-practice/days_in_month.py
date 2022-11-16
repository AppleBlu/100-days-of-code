def is_leap(years):
    if years % 4 == 0:
        if years % 100 == 0:
            if years % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(years, months):
    if months > 12 or months < 1:
        return 'Invalid Input'
    if is_leap(years):
        month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days_leap[months - 1]
    elif not is_leap(years):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return month_days[months - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
if days_in_month(year, month) == 'Invalid Input':
    print('Invalid Input')
else:
    print(f'\nThere are {days_in_month(year, month)} days in that month.')
