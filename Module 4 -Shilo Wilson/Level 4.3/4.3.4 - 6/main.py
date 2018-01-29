"""
Author Shilo Wilson

4) Open a brand-new file and write to it (should write several lines).

5) Open the file from 1) and read it. Display each line.

6) Open the file from 1) and append to it.

"""
import os

def main():
    print '========== 4.3.4 - 4.3.6 =========='
    with open('myfile.txt', 'w+') as outfile:
        i = [str(j) for j in range(10)]
        s = '\n'.join(i)
        outfile.write(s)

    with open('myfile.txt', 'r') as infile:
        data = [i.strip() for i in infile.readlines()]

    for i in data:
        print i

    with open('myfile.txt', 'a') as outfile:
        i =  [str(j) for j in range(10,20)]
        for j in i:
            outfile.write('\n{}'.format(j))

    with open('myfile.txt', 'r') as infile:
        data = [i.strip() for i in infile.readlines()]
    for i in data:
        print i
    os.remove('myfile.txt')

if __name__ == '__main__':
    main()