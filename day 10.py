# Exercises


# 1 - Title format for the name
def format_name(f_name, l_name):
    """Take the name and change it to the title format"""
    if f_name == '' or l_name == '':
        return 'Should not to be empty'

    # comment 1
    f_name_list = list(f_name.lower())
    l_name_list = list(l_name.lower())

    # comment 2
    f_name_list[0] = f_name_list[0].upper()
    l_name_list[0] = l_name_list[0].upper()

    f_name = ''
    l_name = ''

    for letter in f_name_list:
        f_name += letter
    for letter in l_name_list:
        l_name += letter

    return f'{f_name} {l_name}'


# first_name = input("What is your first name? \n")
# last_name = input("What is your last name? \n")
name_string = format_name('anastaSia', '')
print(name_string)


# comment 1 - to list
# f_name_list = []
# l_name_list = []
# for letter in f_name:
#     f_name_list.append(letter)
# for letter in l_name:
#     l_name_list.append(letter)

# comment 2 - title function
# f_name.title()
# l_name.title()


# 2 - Days in Month
def is_leap(is_leap_year):
    if is_leap_year % 4 == 0:
        if is_leap_year % 100 == 0:
            if is_leap_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year_to_check, month_to_check):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_to_check):
        month_days[1] = 29
    return month_days[month_to_check-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
