"""
Author: Shilo Wilson

2) Write code that searches your entire computer for all files of extension py.
Hint: Use os.walk and any necessary string manipulation functions.

3) Write code that searches your entire computer for all pdf files which reside in any directory (at any level) that
contains the string gr in its name.
"""
import os
import re
import glob

def searchforfile(ext, parent_dir, reg = None):
    """
    Searches for all files in the parent directory or sub directories
    given the files extension = ext and the Regular expression returns a match on
    the file name
    :param ext:
    :param parent_dir:
    :param reg:
    :return:
    """
    files = os.walk(parent_dir)
    for i in files:
        if reg:
            for j in i[-1]:
                if j.rsplit('.')[-1] == ext and reg.search(j):
                    if len(i[1]) > 0:
                        for k in i[1]:
                            yield '\\'.join([i[0],k,j])
                    else:
                        yield '\\'.join([i[0],j])
        else:
            for j in i[-1]:
                if j.rsplit('.')[-1] == ext:
                    if len(i[1]) > 0:
                        for k in i[1]:
                            yield '\\'.join([i[0],k,j])
                    else:
                        yield '\\'.join([i[0], j])



def main():
    print '========== 4.3.2 and 4.3.3 =========='
    pys = searchforfile('py', 'C:\\')
    pdf = searchforfile('pdf', 'C:\\', re.compile('gr'))

    for i in pdf:
        print i
    for i in pys:
        print i
    """
    In python 3.6 glob.glob has a recursive option and is likely much faster 
    """

if __name__ == '__main__':
    main()