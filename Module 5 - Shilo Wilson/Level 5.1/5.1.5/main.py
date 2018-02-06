"""
Author: Shilo Wilson

Create a date differential program.  It should do the following:
    a) Prompt the user to enter any date and time.
    b) Prompt the user to enter another date and time.
    c) Subtract the two datetimes and display the result to the user in several seperate ways:
        i) Total number of days
       ii) Total number of hours
      iii) Total number of minutes
       iv) Total number of seconds
        v) Total number of microseconds
       vi) A complete sentance that breaks everything into the correct units

"""
import datetime
from string import Template
from math import floor
import re

def fractionalTime(diff):
    """
    Using the total_seconds method this will return each units in a fractional form
    :param diff:
    :return:
    """
    total_sec = diff.total_seconds()
    total_micro = total_sec * 10**6
    total_min = total_sec / 60.0
    total_hour = total_min / 60.0
    total_day = total_hour / 24.0
    return total_micro, total_sec, total_min, total_hour, total_day

def segmentTime(diff):
    """
    As a timedelta object only has day, seconds, and microseconds as  parameter
    this function will begin with seconds and subtract whole days, hours, minutes
    returning each whole value with the remainder as microseconds
    :param diff:
    :return:
    """
    seconds = diff.total_seconds()
    day = diff.days
    remainder = seconds - day*24*60*60
    hours = floor(remainder/3600)
    remainder -= hours * 3600
    minutes = floor(remainder/60)
    remainder -= minutes * 60
    seconds = floor(remainder/1)
    microseconds = remainder - seconds
    return day, hours, minutes, seconds, microseconds


def main():
    print('========== Exercise 5.1.5 ==========\n ')

    # The following template will be used for the final output
    t= Template('The difference is $days, $hours, $minutes, $seconds, $microseconds')
    dt = datetime.datetime.strptime(raw_input('Please enter a date-time (yyyy:mm:dd:hh:mm:ss:xxxxxx)'),'%Y:%m:%d:%H:%M:%S:%f')
    new_dt = datetime.datetime.strptime(raw_input('Please enter a date-time (yyyy:mm:dd:hh:mm:ss:xxxxxx)'),'%Y:%m:%d:%H:%M:%S:%f')

    diff = new_dt - dt

    micro, sec, mins, hour, day = fractionalTime(diff)
    print('Total number of days: {}'.format(day))
    print('Total number of hours: {}'.format(hour))
    print('Total number of minutes: {}'.format(mins))
    print('Total number of seconds: {}'.format(sec))
    print('Total number of microseconds: {}'.format(micro))
    print(segmentTime(diff))
    day, hours, minutes, seconds, microseconds = segmentTime(diff)
    t_params = dict()

    # Only add the non-zero values.  When using the Template.safe_substitute, the $unit flag will remain
    if day:
        t_params['days'] = '{0} days'.format(day)
    if hours:
        t_params['hours'] = '{0} hours'.format(hours)
    if minutes:
        t_params['minutes'] = '{0} minutes'.format(minutes)
    if seconds:
        t_params['seconds'] = '{0} seconds'.format(seconds)
    if microseconds:
        t_params['microseconds'] = '{0:.6f} microseconds'.format(microseconds)

    # Use regular expression to remove any unit flag which was not included in the final string
    print (re.sub('\$.+?, ','',t.safe_substitute(t_params)))

if __name__ == '__main__':
    main()