"""
Author: Shilo Wilson

2) Save the following Windows file-path into a string variable: C:\Users\Me\Desktop\MyTable.csv.
Perform the following operations:
a. Extract the filename with extension from the path.
b. Extract the file extension only.
c. Add another folder (can name it whatever you'd like) between 'Desktop' and the filename.

"""


def main():
    print('========== 4.1.2 ==========')
    test = 'C:\\Users\\Me\\Desktop\\MyTable.csv'
    route = test.rsplit('\\', 1)
    filename = route[-1]
    extension = filename.rsplit('.')[-1]

    route.insert(-1, 'Loans')
    newpath = '\\'.join(route)

    print('A: Filename is {}'.format(filename))
    print('B: File extension is {}'.format(extension))
    print('C: New path is {}'.format(newpath))


if __name__ == '__main__':
    main()