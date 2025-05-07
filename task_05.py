from datetime import datetime, timedelta

def date_in_future(increment):
    return ((datetime.now()
             if increment is None or type(increment) != int or increment < 0
             else datetime.now() + timedelta(days=increment))
            .strftime("%d-%m-%Y %H:%M:%S"))

print(date_in_future([],))
print(date_in_future(2,))
print(date_in_future(-10))
print(date_in_future(31))
print(date_in_future(1))
print(date_in_future(0))