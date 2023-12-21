from datetime import date
from datetime import timedelta

debugging_mode = False #when 'false' script uses actual current date to check and print upcomming birthdays, when 'true' script uses hardcoded date
current_date = None
current_week = None
monday = []
tuesday = []
wednesday = []
thursday = []
friday = []
celebration_list = []
celebration_list.append(monday)
celebration_list.append(tuesday)
celebration_list.append(wednesday)
celebration_list.append(thursday)
celebration_list.append(friday)

users = [{'name': 'Greg', 'birthday': date(1991, 4, 22)},
         {'name': 'Bill', 'birthday': date(1995, 4, 16)},
         {'name': 'Jill', 'birthday': date(1987, 4, 7)},
         {'name': 'Kim', 'birthday': date(1969, 4, 4)},
         {'name': 'Jan', 'birthday': date(1955, 12, 22)},
         {'name': 'Tommy', 'birthday': date(1999, 1, 11)},
         {'name': 'Rob', 'birthday': date(2002, 12, 29)},
         {'name': 'Simon', 'birthday': date(2004, 8, 21)},
         {'name': 'Ross', 'birthday': date(2000, 4, 17)},
         {'name': 'Sarah', 'birthday': date(1997, 4, 19)},
         ]

def today_date():
    """Funcion for debugging purposes only
    If debugging mode is on it lets you hardcode a today date"""
    if debugging_mode == True:
        return date(2023, 4, 19)
    else:
        return date.today()

def get_celebration_day(birthday_this_year):
    """Funcion takes datetime object as argument
    If date is saturday or sunday adds appropriate timedelta to make it monday
    otherwise it returns unaltered date"""
    if birthday_this_year.weekday() == 5: #check if date is saturday
        celebration_day = birthday_this_year + timedelta(days = 2)
        return celebration_day
    elif birthday_this_year.weekday() == 6: #check if date is sunday
        celebration_day = birthday_this_year + timedelta(days = 1)
        return celebration_day
    else: # if its monday - friday it returns unaltered date
        return birthday_this_year

def create_list_of_upcomming_birthdays():
    """Functions iterates through all users
    if their birthday is due it adds their name to a list"""
    for employee in users:
        birthday = employee.get('birthday') # get birthday from dictionary
        birthday_this_year = date(current_date.year, birthday.month, birthday.day)  #changes birthday year for current year
        birthday_celebration_day = get_celebration_day(birthday_this_year) #get celebration day (saturday and sunday birthdays get postponed to monday)
        birthday_celebration_week = birthday_celebration_day.isocalendar().week #get week of the year for comparison purposes
        birthday_celebration_weekday = birthday_celebration_day.weekday()
        if birthday_celebration_week == current_week:
            celebration_list[birthday_celebration_weekday].append(employee.get('name')) #add employee name to correct list (indexing with weekday)

def celebration_list_report():
    """Funcion prints upcomming birthday in console"""
    result = ""
    for weekday in celebration_list:
        if len(weekday) < 1: #ignoring empty lists
            continue
        else:
            if celebration_list.index(weekday) == 0: #its monday
                result += "Monday: "
            elif celebration_list.index(weekday) == 1: #its tuesday
                result += "Tuesday: "
            elif celebration_list.index(weekday) == 2: #its wednesday
                result += "Wednesday: "
            elif celebration_list.index(weekday) == 3: #its thursday
                result += "Thursday: "
            elif celebration_list.index(weekday) == 4: #its friday
                result += "Friday: "
            for person in weekday:
                result += person + ', '
            result = result.removesuffix(', ') #delete last comma and space
            result += "\n"
    if not result:
        print('No birthdays to celebrate this week')
    else:
        print('This week we are celebrating some birthdays!')
        print(result)
            
if __name__ == '__main__':
    current_date = today_date()
    current_week = current_date.isocalendar().week
    print(f'Current date is {current_date} and current week is {current_week}. Today is {current_date.strftime("%A")}')
    create_list_of_upcomming_birthdays()
    celebration_list_report()
