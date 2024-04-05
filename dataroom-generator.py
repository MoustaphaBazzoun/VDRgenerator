import pandas as pd
import os
import typer

#Basic Logic
"""
Notes:
- Maybe temp and result can be improved
- Split some logic into small functions to make it easier to read
"""

app = typer.Typer()

@app.command()
def generate(filename_input):

    os.mkdir("./DataRoom")

    df = pd.read_excel(str(filename_input), header=0, converters={"Number":str, "File":str})

    dfToDict = {}

    for index, row in df.iterrows():
        dfToDict[row['Number']] = row['File']


    for key in dfToDict:
        splittedA = key.split(sep=".")
        result = "./DataRoom"
        temp = ""
        for n in splittedA:
            if temp == "":
                temp = str(n)
            else:
                temp = temp + "." + str(n)
            result = result + "/" + str(temp) + "." + str(dfToDict[temp])
        print(result)
        os.mkdir(result)

@app.command()
def autosort():
    print("Sorter")

if __name__ == "__main__":
    app()