from datetime import datetime,timezone

def toutc(value):
    if value == None:
        return None
    print(1212,value)
    if value.tzname() == None:
        return datetime(
            value.year,
            value.month,
            value.day,
            value.hour,
            value.minute,
            value.second,
            value.microsecond,
            tzinfo=timezone.utc
        )
    else:
        return value