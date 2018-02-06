"""
Author: Shilo Wilson

Create a date calculator program.  It should do the following:
    a) Prompt the user to enter any date and time
    b) Prompt the user to enter a delta time that is used to add or subtract from the original
    c) Display the calculated resulting date and time, in an easily readable format
"""
import datetime
import operator

def main():
    print('========== Exercise 5.1.4 ==========\n ')
    opt_dict = {'+': operator.add,
                '-': operator.sub}

    dt = datetime.datetime.strptime(raw_input('Please enter a date-time (yyyy:mm:dd:hh:mm:ss:xxxxxx)'),'%Y:%m:%d:%H:%M:%S:%f')
    diff = raw_input('Please enter a time difference (+/-hh:mm:ss:xxxxxx)')

    h, m, s, m_s = diff.split(':')

    if diff[0] in opt_dict.keys():
        """
        Testing to see if the value was signed, if not it is assumed to be positive
        """
        delta = datetime.timedelta(hours = float(h[1:]), minutes = float(m),
                           seconds = float(s), microseconds = float(m_s))
        op = opt_dict[diff[0]]
    else:
        delta = datetime.timedelta(hours=float(h), minutes=float(m),
                           seconds=float(s), microseconds=float(m_s))
        op = operator.add

    new_dt = op(dt, delta)

    print'The new date time is: {}'.format(new_dt.strftime('%Y-%m-%d %H:%M:%S:%f'))

if __name__ == '__main__':
    main()