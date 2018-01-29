""""
Author: Shilo Wilson

1) To practice file management, do the following in order (using Python code):
a. Create a new directory.
b. Rename the above directory.
c. Delete the above directory.
d. Create another directory and create two text files in this directory.
e. Delete one of the text files from the above directory.
f. Rename the remaining text file.
g. Create a subdirectory within the above created directory.
h. Move the remaining text file into the subdirectory.
i. Remove the top level directory with all its contents (using a single function call). Be careful!

"""
import os
import shutil


def main():
    print('========== Exercise 4.3.1 =========')

    os.mkdir('C:\Test_Directory')
    os.rename('C:\Test_Directory', 'C:\Test_DirectoryNew')
    os.rmdir('C:\Test_DirectoryNew')
    os.mkdir('C:\Test_Directory')
    f1 = open('C:\\Test_Directory\\File1.txt', 'w')
    f2 = open('C:\\Test_Directory\\File2.txt','w')
    f1.close(); f2.close()
    os.remove('C:\\Test_Directory\\File2.txt')
    os.rename('C:\\Test_Directory\\File1.txt','C:\\Test_Directory\\File2.txt')
    os.mkdir('C:\\Test_Directory\\Sub_Directory')
    os.rename('C:\\Test_Directory\\File2.txt', 'C:\\Test_Directory\\Sub_Directory\\File2.txt')
    shutil.rmtree('C:\\Test_Directory')
    print('Complete')


if __name__ == '__main__':
    main()