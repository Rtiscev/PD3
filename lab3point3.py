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
hashset2 = set()
actualYear = ""
lastMonth = ""
fMonth = ""
string = ""
weekCounter = 0
fDay = 0

for i in range(len(lines)):
    # get the I'th line from the file and split it
    sliced = lines[i].split(",")

    # get current Year
    actualYear = sliced[0]

    if actualYear.split("/")[0] not in hashset:
        hashset2.clear()
    # save only the month
    hashset2.add(actualYear.split("/")[1])

    # save only the year
    hashset.add(actualYear.split("/")[0])

    # save first Month
    if arr == []:
        fDay = sliced[1]
        fMonth = actualYear

    # prepare array with the Data from file
    for rr in range(len(sliced)):
        if rr > 0 and rr < len(sliced) - 1:
            string += sliced[rr] + ","
        elif rr > 0:
            string += sliced[rr]
    # append the string
    arr.append(string)

    # go next week
    weekCounter += 1

    if actualYear == "2022/11":
        A = 5

    # get next Year
    if i < len(lines) - 1:
        nextYear = lines[i + 1].split(",")[0]
    else:
        nextYear = "EOF"

    # if reached the end of file or the nextYear has not been added to the set
    if (
        nextYear.split("/")[0] not in hashset
        or nextYear.split("/")[1] not in hashset2
        or nextYear == "EOF"
        or weekCounter == 7
    ):
        actualYear = (
            fixString(actualYear) + "/" + (fDay if len(fDay) == 2 else "0" + fDay)
        )
        endOfYear = (
            fixString(fMonth)
            + "/"
            + (sliced[1] if len(sliced[1]) == 2 else "0" + sliced[1])
        )

        # concatenate the string with new and old date
        fName = actualYear.replace("/", "") + "_" + endOfYear.replace("/", "")

        # open file and write to it
        with open(f"files\weeks\{fName}.csv", "w") as file:
            for item in arr:
                file.write(item)

        # nullify the array
        arr = []

        # nullify the weekCounter
        weekCounter = 0

    # nullify the string after the loop iteration (always)
    string = ""
