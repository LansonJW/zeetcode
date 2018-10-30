import datetime

def print_header():
    print('---------------------')
    print('birthday app')
    print('---------------------')


def get_birthday_from_user():
    print('when were you born?')
    year = int(input('year [YYYY]: '))
    # print(len(year))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates():
    pass


def print_birthday_information():
    pass


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    now = None
    # number_of_days = compute_days_between_dates(bday, now)
    # print_birthday_information(number_of_days)

main()