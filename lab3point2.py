import os


def fixString(source):
    prepareStr = source.split("/")
    if len(prepareStr[1]) < 2:
        source = prepareStr[0] + "/" + "0" + prepareStr[1]
    return source


f = open("dataset.csv", "r")
lines = f.readlines()

arr = []
hashset = set()
actualYear = ""
lastMonth = ""
fMonth = ""
string = ""

for i in range(len(lines)):
    # get the I'th line from the file and split it
    sliced = lines[i].split(",")

    # get current Year
    actualYear = sliced[0]
    # save only the year
    hashset.add(actualYear.split("/")[0])

    # save first Month
    if arr == []:
        fMonth = actualYear

    # prepare array with the Data from file
    for rr in range(len(sliced)):
        if rr > 0 and rr < len(sliced) - 1:
            string += sliced[rr] + ","
        elif rr > 0:
            string += sliced[rr]
        elif rr == 0:
            temp = actualYear.split("/")
            if len(temp[1]) < 2:
                string += "0" + temp[1] + ","
            else:
                string += temp[1] + ","
    # append the string
    arr.append(string)

    # get next Year
    if i < len(lines) - 1:
        nextYear = lines[i + 1].split(",")[0]
    else:
        nextYear = "EOF"

    if nextYear.split("/")[0] not in hashset or nextYear == "EOF":
        actualYear = fixString(actualYear)
        endOfYear = fixString(fMonth)

        fName = actualYear.replace("/", "") + "_" + endOfYear.replace("/", "")
        with open(f"files\months\{fName}.csv", "w") as file:
            for item in arr:
                file.write(item)

        arr = []

    string = ""
