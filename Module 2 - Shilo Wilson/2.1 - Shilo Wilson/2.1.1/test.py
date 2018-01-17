from Timer import Timer as Timer
import time

def main():

    """
    Below test that Timer default unit is seconds
    error message when starting a started timer and
    error message when ending a non-started timer.

    """
    print ('========== Exercise 2.1.1 ==========')
    t = Timer()
    t.start()
    t.start()
    time.sleep(1)
    t.end()
    t.end()
    print(t.unit)

    """
    Below ensures that the units are being changed accordingly
    """
    t.unit = 'm'
    t.start()
    time.sleep(2)
    t.end()
    print(t.prevtime)
    print(t.unit)


if __name__ == '__main__':
    main()
