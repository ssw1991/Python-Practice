"""
Author: Shilo Wilson

Write code that generates a list of 200,000 uniform random numbers, ranging from 1 to 20.
Additionally, generate 200,000 normally distributed random numbers (mu=10, sigma=7) and
200,000 lognormally distributed random numbers (mu=1, sigma=0.5). Export these lists of numbers
to a single CSV file (should have 200,000 rows and three columns):
a. Open this CSV file in Excel.
b. Create three additional Excel Worksheets (named Uniform, Normal, and Lognormal).
Name the original Worksheet 'Input'.
c. In each Worksheet, create a Histogram corresponding to its input data column (Insert>Histogram).
d. Notice how the Uniform graph appears almost flat, the normal graph appears to be a bell
curve, and the lognormal graph appears to be a bell curve with a large tail.
This is an example of convergence due to the Law of Large Numbers: If you generate enough
random numbers using a certain distribution, it will always start to converge to the distribution.
Note that you will need to save the result as an Excel spreadsheet (.xlsx) instead of .csv for
submission

"""

import random


def normalize(vals):
    maxn = 100
    minn = 1
    maxo = max(vals.values())
    mino = min(vals.values())

    for i in vals.keys():
        vals[i] = (maxn - minn)/(maxo + mino) * (vals[i] - maxo) + maxn
    return vals

def output(vals):
    for i in sorted(vals.keys()):
        print('{}: {}'.format(i, ''.join(['-' for k in range(vals[i])])))
def main():

    dists = ((round(random.uniform(0, 20)), round(random.normalvariate(10, 7)), round(random.lognormvariate(1, 0.5))) for i in xrange(200000))

    uni = {}
    norm = {}
    log = {}


    with open('data.csv', 'w+') as outfile:
        for i in dists:
            u , n, l = i

            if u in uni:
                uni[u] += 1
            else:
                uni[u] = 1

            if n in norm:
                norm[n] += 1
            else:
                norm[n] = 1

            if l in log:
                log[l] += 1
            else:
                log[l] = 1

        print('========= Uniform Dist ==========')
        output(uni)
        print('========= Normal Dist ==========')
        output(norm)
        print('========= Log Normal Dist ==========')
        output(log)

if __name__ == '__main__':
    main()