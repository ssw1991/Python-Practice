"""
Author: Shilo Wilson

Main file to test asset.py
"""
from asset import Asset as Asset

def main():
    print ( '========== Exercise 2.1.6 ==========')
    myAsset = Asset(10000)

    print ('Initial Value: {}'.format(myAsset.initialvalue))
    print ('Monthly Depreciation: {}'.format(myAsset.monthlyDepriciation()))
    print ('Annual Depreciation: {}'.format(myAsset.yearlyDepreciation()))
    myAsset.initalvalue = 12000
    print ('New Inital Value: {}'.format(myAsset.initialvalue))

    print(myAsset.currentvalue(8))

if __name__ == '__main__':
    main()
