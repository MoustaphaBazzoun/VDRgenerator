import pandas as pd
import os

#df = pd.read_excel("potato.xlsx")

#print(df.head())

testDict = {
    '1':'Financials',
    '1.1':'Income Statement',
    '1.2':'Balance Sheet',
    '1.2.1':"Hello",
    '2':'Operational',
    '2.1':'Revenue',
    '2.2':'Costs',
    '2.3':'Payment Roll',
    '3':'Legal',
}

#Basic Logic
"""
Notes:
- Maybe temp and result can be improved
- Split some logic into small functions to make it easier to read
"""
for key in testDict:
    splittedA = key.split(sep=".")
    result = "./DataRoom"
    temp = ""
    for n in splittedA:
        if temp == "":
            temp = str(n)
        else:
            temp = temp + "." + str(n)
        result = result + "/" + str(temp) + "." + str(testDict[temp])
    print(result)
    os.mkdir(result)

