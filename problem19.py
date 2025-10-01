import datetime

def sunday_count():
    start_date = datetime.date(1901,1,1)
    end_date = datetime.date(2000,12,31)
    current = start_date
    total = 0
    while current <= end_date:
        if current.weekday() == 6 and current.day == 1:
            total += 1
        current += datetime.timedelta(days=1)
    return total

print(sunday_count())