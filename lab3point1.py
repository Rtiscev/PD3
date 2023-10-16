import os

f = open("dataset.csv", "r")
lines = f.readlines()

# if it exists, delete it
if os.path.exists("files\X.csv"):
    os.remove("files\X.csv")
if os.path.exists("files\Y.csv"):
    os.remove("files\Y.csv")

X = open("files\X.csv", "a")
Y = open("files\Y.csv", "a")


for line in lines:
    txt = line.split(",")
    i = 0
    string = ""
    for text in txt:
        if i == 0:
            X.write(f"{text}\n")
        elif i == len(txt) - 1:
            string += text
        else:
            string += text + ","
        i += 1
    Y.write(string)

X.close()
Y.close()
