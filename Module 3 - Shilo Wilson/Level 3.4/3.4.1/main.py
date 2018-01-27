"""
Author: Shilo Wilson

1) Open a file and write to it, using the with statement. Verify that the file has indeed been closed, once the with
statement exits (check the closed attribute on the file handle variable).
"""


def main():

    with open('test.txt', 'w+') as outfile:
        outfile.write('This is a test')
    print(outfile.closed)


if __name__ == '__main__':
    main()