"""
Author: Shilo Wilson
1) We've been using time.time before and after code blocks to report the difference as time taken. This exercise
is to generalize and encapsulate this into a class, to make things cleaner and re-usable.  The steps are as follows:

a.	Create a class called Timer.
b.	Add a start method and end method. They should work as follows:

c.	Note that start should give an error if the Timer is already started and end should give an error if the Timer is not
currently running.
d.	Add the ability to configure the Timer to display either seconds, minutes, or hours.
e.	Add a method to retrieve the last timer result.
f.	Test your class thoroughly.

"""

import time


class Timer(object):

    _unitMap = {'s': (1, 'seconds'), 'm': (60, 'minutes'), 'h': (3600, 'hours')}

    def __init__(self, unit = None):
        self._starttime = None
        self._prevtime  = None
        self._unit = unit if unit is not None else Timer._dunit if hasattr(Timer, '_dunit') else 's'

    @classmethod
    def defaultUnit(cls, iunit):
        cls._dunit = iunit

    @property
    def starttime(self):
        return self._starttime

    @property
    def prevtime(self):
        return self._prevtime

    @property
    def unit(self):
        return self._unit

    @unit.setter
    def unit(self, iunit):
        self._unit = iunit if iunit in ['s', 'm', 'h'] else Timer._dunit if hasattr(Timer, '_dunit') else 's'

    def start(self):
        if not self._starttime:
            self._starttime = time.time()
        else:
            print 'Timer already started'


    def end(self):

        if self._starttime:
            self._prevtime = time.time() - self.starttime
            print 'Timer stopped at {} {}'.format(self.prevtime/Timer._unitMap[self._unit][0], Timer._unitMap[self._unit][1])
            self._starttime = None
        else:
            print 'Error, timer never started'
