
def main():
    #
    inputFile = open("Presidents.txt","r")
    print("(1) Using read(number)")
    s1 = inputFile.read(5)
    print(s1)
    s2 = inputFile.read(15)
    print(repr(s2))
    inputFile.close()


    inputFile = open("Presidents.txt","r")
    print("(2) Using read(number)")