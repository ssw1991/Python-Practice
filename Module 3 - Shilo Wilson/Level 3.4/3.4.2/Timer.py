import time


class Timer(object):

    _unitMap = {'s':(1, 'seconds'),'m':(60, 'minutes'),'h':(3600, 'hours')}

    def __init__(self, timerName, unit = None):
        self._timerName = timerName
        self._starttime = None
        self._prevtime  = None
        self._unit = unit if unit is not None else Timer._dunit if hasattr(Timer, '_dunit') else 's'

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.end()

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
            print 'Timer already started'


    def end(self):
        if self._starttime:
            self._prevtime = time.time() - self.starttime
            print '{0} stopped at {1:.16f} {2}'.format(self._timerName, self.prevtime/Timer._unitMap[self._unit][0], Timer._unitMap[self._unit][1])
            self._starttime = None
        else:
            print 'Error, timer never started'

    @unit.setter
    def unit(self, iunit):
        self._unit = iunit if iunit in ['s','m','h'] else Timer._dunit if hasattr(Timer, '_dunit') else 's'

    def configureTimerDisplay(self, display):
        self.unit = display

