import collections


def readFile(fileName):
    f = open(fileName, "r")
    return f.readlines()


if __name__ == "__main__":

    bagOfWords = {}

    bagOfWords[0] = "aaa"
    bagOfWords[1] = "bbb"
    bagOfWords[2] = "ccc"
    bagOfWords[3] = "ddd"
