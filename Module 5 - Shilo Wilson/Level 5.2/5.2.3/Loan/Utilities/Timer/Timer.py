import time
import logging
logger = logging.getLogger('__main__.{}'.format(__name__))
from functools import wraps

class Timer(object):
    _unitMap = {'s':(1, 'seconds'),'m':(60, 'minutes'),'h':(3600, 'hours')}
    _warnThreshold = 60

    def __init__(self, fn = None, unit = None):
        self._starttime = None
        self._prevtime  = None
        self._fn = fn
        self._unit = unit if unit is not None else Timer._dunit if hasattr(Timer, '_dunit') else 's'

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.end()

    def __call__(self, *args, **kwargs):
        """
        Allowing the class to be used as a decorator, so that
        timer can still be used with context managers, as well
        as by deccorating a function.

        However, I am no longer able to set the units when it is
        used as a decorator.

        :param args:
        :param kwargs:
        :return:
        """
        start = time.time()
        x = self._fn(*args, **kwargs)
        end = time.time()
        print 'Time taken for {0}: {1:.6f} {2}'.format(self._fn, (end - start)/Timer._unitMap[self._unit][0], Timer._unitMap[self._unit][1])
        return x


    @classmethod
    def threshold(cls, time):
        if time > cls._warnThreshold:
            logger.warn('Operation took longer than {} seconds'.format(cls._warnThreshold))

    @classmethod
    def defaultUnit(cls, iunit):
        cls._dunit = iunit

    @property
    def timerName(self):
        return self._timerName

    @property
    def starttime(self):
        return self._starttime

    @property
    def prevtime(self):
        return self._prevtime

    @property
    def unit(self):
        return self._unit

    @timerName.setter
    def timerName(self,itimername):
        self._timerName = itimername

    def start(self):
        if not self._starttime:
            self._starttime = time.time()
        else:
            logger.info('Timer already started')


    def end(self):
        if self._starttime:
            self._prevtime = time.time() - self.starttime
            Timer.threshold(self._prevtime)
            logger.info('{0} stopped at {1:.8f} {2}'.format(self._timerName, self.prevtime/Timer._unitMap[self._unit][0], Timer._unitMap[self._unit][1]))
            self._starttime = None
        else:
            logger.info('Error, timer never started')

    @unit.setter
    def unit(self, iunit):
        if iunit not in ['s','m','h']:
            logger.warn('Not valid parameter, will be set to seconds')
        self._unit = iunit if iunit in ['s','m','h'] else Timer._dunit if hasattr(Timer, '_dunit') else 's'

    def configureTimerDisplay(self, display):
        self.unit = display

