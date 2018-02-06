""""
Author: Shilo Wilson

1) Create a program that does the following:
    a) Ask the user to input year, month, day, hour, minute, second, microsecond (one after another).
    b) Createa a datetime variable with the entered info.
    c) Extract the datetime into your year, month, day, hour, minutes, second, and microsecond.
    Display the following result
    d) Display the entered datetime with the following format: yyyy-mm-dd hr:mm:ss:xxxxx
    e) Display the entered datetime with the following format: yyyy Month hr:mm:ss:xxxxx (am/pm)
    f) Do d-e with the current local time
    g) Do parts d-e with the current UTC time

"""
import datetime as datetime
import pytz


def main():

    """

    It is unclear whether the "one after another" meant to query the user once,
    and ask for all elements, or to query the user individually for each element.


    """
    year = int(raw_input('Please enter a year (yyyy): '))
    month = int(raw_input('Please enter a Month (mm): '))
    day = int(raw_input('Please enter a day (dd): '))
    hour = int(raw_input('Please enter the hour (hh): '))
    minute = int(raw_input('Please enter the minutes (mm): '))
    second = int(raw_input('Please enter the seconds (ss): '))
    m_second = int(raw_input('Please enter the microseconds (xxxxxx): '))

    date = datetime.datetime(year, month, day, hour, minute, second, m_second)

    # The following will output in local standard time.
    print('Year: {0}\n'
          'Month: {1}\n'
          'Day: {2}\n'
          'Hour: {3}\n'
          'Minutes: {4}\n'
          'Seconds: {5}\n'
          'Microsecond: {6}\n'.format (date.year, date.month, date.day, date.hour, date.minute, date.second, date.microsecond))
    print('Local Time: {}'.format(date.strftime('%Y-%m-%d %H:%M:%S:%f')))
    print('Local Time {}'.format(date.strftime('%Y %B-%d %I:%M:%S:%f %p')))


    # Previous was done in local, now to convert to UTC
    localtz = pytz.timezone('US/Eastern')
    local_dt = localtz.localize(date, is_dst=None)
    utc_date = local_dt.astimezone(pytz.utc)

    print('UTC Time: {}'.format(utc_date.strftime('%Y-%m-%d %H:%M:%S:%f')))
    print('UTC Time: {}'.format(utc_date.strftime('%Y %B %d %I:%M:%S:%f %p')))

if __name__ == '__main__':
    main()