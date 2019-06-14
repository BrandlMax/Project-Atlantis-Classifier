# Max Shitty Data Parser
def get(txtFile):
    Data = []
    dataTxt = open(txtFile, "r")
    # single ['123,456','123,456','123,456',...]
    dataListWithStrings = dataTxt.read().split()

    # single ['123,456', ...] -> [[123, 456], ...]
    for single in dataListWithStrings:
        singleStringList = single.split(",")
        parsedList = []
        for singleItem in singleStringList:
            parsedList.append(int(singleItem))
        Data.append(parsedList)

    return Data
