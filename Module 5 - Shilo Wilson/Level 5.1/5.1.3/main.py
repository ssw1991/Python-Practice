""""
Author: Shilo Wilson

2) Modify the above program to request the user enter the date in the following format (for example):
2016 September 25 06:24:14:12342 PM

"""
import datetime as datetime
import pytz


def main():

    date_string = raw_input('Please enter the date and time (YYYY Month DD hh:mm:ss:micro AM/PM): ')
    date = datetime.datetime.strptime(date_string, '%Y %B %d %I:%M:%S:%f %p')

    # The following will output in local standard time.
    print('Year: {0}\n'
          'Month: {1}\n'
          'Day: {2}\n'
          'Hour: {3}\n'
          'Minutes: {4}\n'
          'Seconds: {5}\n'
          'Microsecond: {6}\n'.format(date.year, date.month, date.day, date.hour, date.minute, date.second,
                                      date.microsecond))
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