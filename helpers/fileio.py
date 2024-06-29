
def saveItemsOutput(jsonValue):
    file_object = open("savedItems.json", "w")
    file_object.write(jsonValue)
    file_object.close()

def readItemsOutput():
    output = open("savedItems.json", "r").read()
    return output.replace("'", '"')
'''
def saveDetailsOutput(jsonValue):
    file_object = open("savedDetails.txt", "w")
    file_object.write(jsonValue)
    file_object.close()

def readDetailsOutput():
    output = open("savedDetails.txt", "r").read()
    return output.replace("'", '"')
'''