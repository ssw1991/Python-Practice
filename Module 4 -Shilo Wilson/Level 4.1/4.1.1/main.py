"""
Author: Shilo Wilson

a. Display the length of the string.
b. Find the index of the first 'o' in the string.
c. Trim off the leading spaces only.
d. Trim off the trailing spaces only.
e. Trim off both the leading and trailing spaces (use this trimmed string
 for all the remaining parts below).
 f. Fully capitalize the string.
 g. Fully lowercase the string.
 h. Display the number of occurrence of the letter 'd' and of the word
 'the'.
 i. Display the first 15 characters of the string.
 j. Display the last 10 characters of the string.
 k. Display characters 5-23 of the string.
 l. Find the index of the first occurrence of the word 'course'.
 m. Find the index of the second occurrence of the word 'course'.
 n. Find the index of the second to last occurrence of the letter 't',
 between the 7th and 33rd characters in the string.
 o. Replace the period (.) with an exclamation point (!).
 p. Replace all occurrences of the word 'course' with 'class'.
"""


def nth_occurrence(string, substring, n):
    start = string.find(substring)
    while start >= 0 and n > 1:
        start = string.find(substring, start +1)
        n -= 1
    return start


def main():
    mystr =  "    The Python course is the best course that I have ever taken.       "

    print('A: Length of string is {}'.format(len(mystr)))
    print('B: First o occurs at index {}'.format(mystr.index('o')))
    print('C: {}'.format(mystr.lstrip()))
    print('D: {}'.format(mystr.rstrip()))
    mystr = mystr.strip()
    print('E: {}'.format(mystr))
    print('F: {}'.format(mystr.upper()))
    print('G: {}'.format(mystr.lower()))
    print('H: d occurs {0!s} times, the occurs {1!s} times'.format(mystr.count('d'), mystr.count('the')))
    # H will not count 'The'
    print('I: {}'.format(mystr[:15]))
    print('J: {}'.format(mystr[-10:]))
    print('K: {}'.format(mystr[4:23]))
    print('L: First occurrence of course is {0!s}'.format(mystr.find('course')))
    print('M: Second occurrence of course is {0!s}'.format(nth_occurrence(mystr, 'course', 2)))
    num_t = mystr[6:23].count('t')
    print(num_t)
    print('N: Second to last occurrence of t is {0!s}'.format(nth_occurrence(mystr[6:23], 't', num_t - 1)+7))
    mystr = mystr.replace('.', '!')
    print('O: {}'.format(mystr))
    mystr = mystr.replace('course', 'class')
    print('P: {}'.format(mystr))

if __name__ == '__main__':
    main()



