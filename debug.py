from datetime import datetime

UNE_DATE_FORMAT = '%d/%m/%Y'

def main():
    # import ipdb; ipdb.set_trace()
    today = datetime.now()
    my_birthday = '25-11-1988'
    my_birthday_date = datetime.strptime(my_birthday, UNE_DATE_FORMAT)
    difference = today - my_birthday_date
    return difference.days

if __name__ == '__main__':
    days = main()
    print '{} days'.format(days)
