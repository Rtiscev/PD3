import datetime
import os


def firstFunc():
    # first model
    # from dataset.csv
    isFound = False
    isChanged = False
    f = open("dataset.csv", "r")
    lines = f.readlines()
    arr = []
    string = ""

    for i in range(len(lines)):
        sliced = lines[i].split(",")

        # get current month and year
        year = sliced[0].split("/")[0]
        month = sliced[0].split("/")[1]

        if isFound == False and isChanged == True:
            break

        if datetime_object.year == int(year) and datetime_object.month == int(month):
            # prepare array with the Data from file
            for rr in range(len(sliced)):
                if rr > 0 and rr < len(sliced) - 1:
                    string += sliced[rr] + ","
                elif rr > 0:
                    string += sliced[rr]
            # append the string
            arr.append(string)

            if isFound == False:
                isFound = True
            isChanged = True

        string = ""

    return arr


def secondFunc():
    # first model
    # from dataset.csv
    isFound = False
    isChanged = False
    X = open("files/X.csv", "r")
    Y = open("files/Y.csv", "r")
    lines = X.readlines()
    linesY = Y.readlines()
    arr = []
    string = ""

    for i in range(len(lines)):
        sliced = lines[i].split(",")
        slicedY = linesY[i].split(",")

        # get current month and year
        year = sliced[0].split("/")[0]
        month = sliced[0].split("/")[1]

        if isFound == False and isChanged == True:
            break

        if datetime_object.year == int(year) and datetime_object.month == int(month):
            # prepare array with the Data from file
            for rr in range(len(slicedY)):
                if rr < len(slicedY) - 1:
                    string += slicedY[rr] + ","
                elif rr > 0:
                    string += slicedY[rr]
            # append the string
            arr.append(string)

            if isFound == False:
                isFound = True
            isChanged = True

        string = ""

    return arr


def thirdFunc():
    items = os.listdir("files/months")

    foundItem = ""
    for item in items:
        year = item[:4]
        if int(year) == datetime_object.year:
            foundItem = item

    isFound = False
    isChanged = False
    file = open(f"files/months/{foundItem}", "r")
    lines = file.readlines()
    arr = []
    string = ""

    for i in range(len(lines)):
        sliced = lines[i].split(",")

        # get current month
        month = sliced[0]

        if isFound == False and isChanged == True:
            break

        if datetime_object.month == int(month):
            # prepare array with the Data from file
            for rr in range(len(sliced)):
                if rr > 0 and rr < len(sliced) - 1:
                    string += sliced[rr] + ","
                elif rr > 0:
                    string += sliced[rr]
            # append the string
            arr.append(string)

            if isFound == False:
                isFound = True
            isChanged = True

        string = ""

    return arr


def fourthFunc():
    items = os.listdir("files/weeks")

    fileArr = []
    foundItem = ""
    for item in items:
        year = item[:4]
        month = item[4:6]
        if int(year) == datetime_object.year and int(month) == datetime_object.month:
            # foundItem = item
            fileArr.append(item)

    isFound = False
    isChanged = False
    arr = []
    string = ""
    for fileName in fileArr:
        file = open(f"files/weeks/{fileName}", "r")
        lines = file.readlines()

        for i in range(len(lines)):
            sliced = lines[i].split(",")

            # get current month
            month = sliced[0]

            if isFound == False and isChanged == True:
                break

            # prepare array with the Data from file
            for rr in range(len(sliced)):
                if rr < len(sliced) - 1:
                    string += sliced[rr] + ","
                elif rr > 0:
                    string += sliced[rr]
            # append the string
            arr.append(string)

            if isFound == False:
                isFound = True
            isChanged = True

            string = ""

    return arr


def callFunc(choice):
    if choice == 1:
        if firstFunc() == []:
            print("None")
        else:
            for item in firstFunc():
                print(item)
    elif choice == 2:
        if secondFunc() == []:
            print("None")
        else:
            for item in secondFunc():
                print(item)
    elif choice == 3:
        if thirdFunc() == []:
            print("None")
        else:
            for item in thirdFunc():
                print(item)
    elif choice == 4:
        if fourthFunc() == []:
            print("None")
        else:
            for item in fourthFunc():
                print(item)


def accept_datetime():
    datetime_string = input("Enter a datetime as : ")

    datetime_object = None

    try:
        format_string = "%Y-%m"
        datetime_object = datetime.datetime.strptime(datetime_string, format_string)
    except:
        try:
            format_string = "%Y,%m"
            datetime_object = datetime.datetime.strptime(datetime_string, format_string)
        except:
            format_string = "%Y %m"
            datetime_object = datetime.datetime.strptime(datetime_string, format_string)
    return datetime_object


datetime_object = accept_datetime()
print(datetime_object)

# callFunc(1)
# callFunc(2)
# callFunc(3)
# callFunc(4)
