
def saveItemsOutput(jsonValue):
    file_object = open("../services/f21/savedItems.json", "w")
    file_object.write(jsonValue)
    file_object.close()

def readItemsOutput():
    output = open("savedItems.json", "r").read()
    return output.replace("'", '"')

def saveDetailsOutput(jsonValue):
    file_object = open("savedDetails.json", "w")
    file_object.write(jsonValue)
    file_object.close()

def readDetailsOutput():
    output = open("savedDetails.json", "r").read()
    return output.replace("'", '"')