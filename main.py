import datetime as dtm
from plumbum import colors
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    today = dtm.datetime.date(dtm.datetime.now())
    with colors.red:
        print(f"Живем в интересное время, а точнее {today}")

