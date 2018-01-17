# coding=utf-8
"""
Name:  Shilo S Wilson

Exercise: 1.5.2

Create two sets: Set 1 should contain the twenty most common male first names in the United States and Set 2 should
contain the twenty most common male first names in Britain (Google it). Perform the following:
    a. Find the first names that appear in both sets.
    b. Find the first names that appear in the United States set, but not Britain.
    c. Find the first names that appear in the Britain set, but not United States.

"""





def main():

    print('============= Exercise 1.5.2 =============\n\n\n')

    usCommon= set(['jacob', 'michael','joshua', 'matthew', 'ethan',
                   'andrew', 'daniel', 'anthony', 'christopher', 'joseph',
                   'william', 'alexander', 'ryan', 'david', 'nicholas',
                   'tyler','james', 'john', 'johnathan', 'nathan'])

    ukCommon = set(['muhammad', 'oliver', 'harry', 'jack','george',
                    'noah', 'leo', 'jacob','oscar', 'charlie',
                    'jackson', 'william', 'joshua', 'ethan', 'james',
                    'freddie', 'alfie', 'logan', 'lucas', 'finley'])

    print 'The following names appear on both list\n'
    print ', '.join(str(o) for o in (usCommon & ukCommon))

    print 'The following names appear on the US list but not the UK\n'
    print ', '.join(str(o) for o in (usCommon - ukCommon))

    print 'The following names appear on UK list but not US\n'
    print ', '.join(str(o) for o in (ukCommon - usCommon))




if __name__ == '__main__':
    main()